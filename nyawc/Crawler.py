# -*- coding: utf-8 -*-

# MIT License
# 
# Copyright (c) 2017 Tijme Gommers
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from nyawc.Queue import Queue, QueueItem
from nyawc.http.Handler import Handler
from nyawc.http.Request import Request
from nyawc.helpers.HTTPRequestHelper import HTTPRequestHelper

import threading
import time

class Crawler:
    """The main Crawler class which handles the crawling recursion, queue and processes.

    Attributes:
        __options (obj): The options to use for the current crawling runtime.
        __queue (obj): The request/response pair queue containing everything to crawl.
        __stopping (bool): If the crawler is topping the crawling process.
        __stopped (bool): If the crawler finished stopping the crawler process.
        __lock (obj): The callback lock to prevent race conditions.

    """

    __options = None

    __queue = Queue()

    __stopping = False

    __stopped = False

    __lock = threading.Lock()

    def __init__(self, options):
        """Constructs a Crawler class.

        Args:
            options (obj): The options to use for the current crawling runtime.

        """

        self.__options = options

    def start_with(self, request):
        """Start the crawler using the given request.

        Args:
            request (obj): The startpoint for the crawler.

        """

        HTTPRequestHelper.patch_with_options(request, self.__options)
        self.__queue.add_request(request)

        self.__crawler_start()

    def __spawn_new_requests(self):
        """Spawn new requests until the max processes option value is reached."""

        concurrent_requests_count = self.__queue.get_count_including([QueueItem.STATUS_IN_PROGRESS])
        new_requests_spawned = False

        while concurrent_requests_count < self.__options.performance.max_threads:
            if self.__spawn_new_request():
                new_requests_spawned = True
                concurrent_requests_count += 1
            else:
                break

        if concurrent_requests_count == 0 and not new_requests_spawned and not self.__stopping:
            self.__crawler_stop()

    def __spawn_new_request(self):
        """Spawn the first queued request if available.

        Returns:
            bool: If a new request was spawned.

        """

        first_in_line = self.__queue.get_first(QueueItem.STATUS_QUEUED)
        if first_in_line is None:
            return False

        self.__request_start(first_in_line)
        return True

    def __crawler_start(self):
        """Spawn the first X queued request, where X is the max processes option."""

        self.__options.callbacks.crawler_before_start()

        try:
            self.__spawn_new_requests()

            while not self.__stopped: 
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            pass

    def __crawler_stop(self, force_quit=False):
        """Mark the crawler as stopped.

        Note:
            If self.__stopped is True, the main thread will be stopped. Every piece of code that gets
            executed after self.__stopped is True could cause Thread exceptions and or race conditions.

        Args:
            force_quit (bool): Also cancel any ongoing requests.

        """

        self.__stopping = True

        queued_items = self.__queue.get_all_including([
            QueueItem.STATUS_QUEUED, 
            QueueItem.STATUS_IN_PROGRESS
        ])

        for queue_item in queued_items:
            queue_item.status = QueueItem.STATUS_CANCELLED

        self.__crawler_finish()

        self.__stopped = True

    def __crawler_finish(self):
        """Called when the crawler is finished because there are no queued requests left or it was stopped."""

        self.__options.callbacks.crawler_after_finish(self.__queue)

    def __request_start(self, queue_item):
        """Execute the request in given queue item.

        Args:
            queue_item (obj): The request/response pair to scrape.

        """

        action = self.__options.callbacks.request_before_start(self.__queue, queue_item)

        if action == CrawlerActions.DO_STOP_CRAWLING:
            self.__crawler_stop(True)
            return

        if action == CrawlerActions.DO_SKIP_TO_NEXT:
            queue_item.status = QueueItem.STATUS_FINISHED
            return

        if action == CrawlerActions.DO_CONTINUE_CRAWLING or action is None:
            queue_item.status = QueueItem.STATUS_IN_PROGRESS

            thread = CrawlerThread(self.__request_finish, self.__lock, queue_item)
            thread.daemon = True
            thread.start()

    def __request_finish(self, queue_item, new_requests):
        """Called when the crawler finished the given queued item.

        Args:
            queue_item (obj): The request/response pair that finished.
            new_requests list(obj): All the requests that were found during this request.

        """

        new_queue_items = []
        action = None

        if queue_item.status not in [QueueItem.STATUS_ERRORED, QueueItem.STATUS_CANCELLED]:
            for new_request in new_requests:
                HTTPRequestHelper.patch_with_options(new_request, self.__options, queue_item.response)
                
                if HTTPRequestHelper.is_already_in_queue(new_request, self.__queue):
                    continue

                if not HTTPRequestHelper.complies_with_scope(self.__queue, queue_item, new_request, self.__options.scope):
                    continue

                new_request.depth = queue_item.request.depth + 1
                if self.__options.scope.max_depth is not None:
                    if new_request.depth > self.__options.scope.max_depth:
                        continue

                new_queue_item = self.__queue.add_request(new_request)
                new_queue_items.append(new_queue_item)

            queue_item.status = QueueItem.STATUS_FINISHED
            action = self.__options.callbacks.request_after_finish(self.__queue, queue_item, new_queue_items)

        if self.__stopping:
            return

        if action == CrawlerActions.DO_STOP_CRAWLING:
            self.__crawler_stop()
            return

        if action == CrawlerActions.DO_CONTINUE_CRAWLING or action is None:
            self.__spawn_new_requests()
            return

class CrawlerThread(threading.Thread):
    """The crawler thread executes the HTTP request using the HTTP handler.

    Attributes:
        __callback (obj): The method to call when finished
        __callback_lock (bool): The callback lock that prevents race conditions.
        __queue_item (obj): The queue item containing a request to execute.

    """

    __callback = None

    __callback_lock = None

    __queue_item = None

    def __init__(self, callback, callback_lock, queue_item):
        """Constructs a crawler thread class

        Args:
            callback (obj): The method to call when finished
            callback_lock (bool): The callback lock that prevents race conditions.
            queue_item (obj): The queue item containing a request to execute.

        """

        threading.Thread.__init__(self)
        self.__callback = callback
        self.__queue_item = queue_item
        self.__callback_lock = callback_lock

    def run(self):
        """Executes the HTTP call.

        Note:
            If the this and the parent handler raised an error, the queue item status will be set to errored
            instead of finished.

        """

        new_requests = []
            
        try:
            handler = Handler(self.__queue_item)
            new_requests = handler.get_new_requests()

            try:
                self.__queue_item.response.raise_for_status()
            except Exception:
                if self.__queue_item.request.parent_raised_error:
                    self.__queue_item.status = QueueItem.STATUS_ERRORED
                else:
                    for new_request in new_requests:
                        new_request.parent_raised_error = True

        except Exception as e:
            self.__queue_item.status = QueueItem.STATUS_ERRORED


        for new_request in new_requests:
            new_request.parent_url = self.__queue_item.request.url

        with self.__callback_lock:
            self.__callback(self.__queue_item, new_requests)

class CrawlerActions:
    """The actions that crawler callbacks can return.

    Attributes:
        DO_CONTINUE_CRAWLING (int): Continue by crawling the request.
        DO_SKIP_TO_NEXT (int): Skip the current request and continue with the next one in line.
        DO_STOP_CRAWLING (int): Stop crawling and quit ongoing requests.
        
    """

    DO_CONTINUE_CRAWLING = 1

    DO_SKIP_TO_NEXT = 2

    DO_STOP_CRAWLING = 3