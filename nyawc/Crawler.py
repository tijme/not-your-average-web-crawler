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

import time
import threading

from nyawc.Queue import Queue
from nyawc.QueueItem import QueueItem
from nyawc.CrawlerThread import CrawlerThread
from nyawc.CrawlerActions import CrawlerActions
from nyawc.helpers.HTTPRequestHelper import HTTPRequestHelper

class Crawler:
    """The main Crawler class which handles the crawling recursion, queue and processes.

    Attributes:
        queue (:class:`nyawc.Queue`): The request/response pair queue containing everything to crawl.
        __options (:class:`nyawc.Options`): The options to use for the current crawling runtime.
        __stopping (bool): If the crawler is topping the crawling process.
        __stopped (bool): If the crawler finished stopping the crawler process.
        __lock (obj): The callback lock to prevent race conditions.

    """

    def __init__(self, options):
        """Constructs a Crawler instance.

        Args:
            options (:class:`nyawc.Options`): The options to use for the current crawling runtime.

        """

        self.queue = Queue(options)
        self.__options = options
        self.__stopping = False
        self.__stopped = False
        self.__lock = threading.Lock()

    def start_with(self, request):
        """Start the crawler using the given request.

        Args:
            request (:class:`nyawc.http.Request`): The startpoint for the crawler.

        """

        HTTPRequestHelper.patch_with_options(request, self.__options)
        self.queue.add_request(request)

        self.__crawler_start()

    def __spawn_new_requests(self):
        """Spawn new requests until the max processes option value is reached.

        Note:
            If no new requests were spawned and there are no requests in progress
            the crawler will stop crawling.

        """

        concurrent_requests_count = self.queue.count_in_progress
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
        """Spawn the first queued request if there is one available.

        Returns:
            bool: If a new request was spawned.

        """

        first_in_line = self.queue.get_first(QueueItem.STATUS_QUEUED)
        if first_in_line is None:
            return False

        self.__request_start(first_in_line)
        return True

    def __crawler_start(self):
        """Spawn the first X queued request, where X is the max threads option.

        Note:
            The main thread will sleep until the crawler is finished. This enables
            quiting the application using sigints (see http://stackoverflow.com/a/11816038/2491049)

        """

        self.__options.callbacks.crawler_before_start()

        try:
            self.__spawn_new_requests()

            while not self.__stopped:
                time.sleep(1)
        except (KeyboardInterrupt, SystemExit):
            self.__crawler_stop()

    def __crawler_stop(self):
        """Mark the crawler as stopped.

        Note:
            If :attr:`__stopped` is True, the main thread will be stopped. Every piece of code that gets
            executed after :attr:`__stopped` is True could cause Thread exceptions and or race conditions.

        """

        if self.__stopping:
            return

        self.__stopping = True

        for status in [QueueItem.STATUS_QUEUED, QueueItem.STATUS_IN_PROGRESS]:
            for queue_item in list(self.queue.get_all(status).values()):
                self.queue.move(queue_item, QueueItem.STATUS_CANCELLED)

        self.__crawler_finish()

        self.__stopped = True

    def __crawler_finish(self):
        """Called when the crawler is finished because there are no queued requests left or it was stopped."""

        self.__options.callbacks.crawler_after_finish(self.queue)

    def __request_start(self, queue_item):
        """Execute the request in given queue item.

        Args:
            queue_item (:class:`nyawc.QueueItem`): The request/response pair to scrape.

        """

        action = self.__options.callbacks.request_before_start(self.queue, queue_item)

        if action == CrawlerActions.DO_STOP_CRAWLING:
            self.__crawler_stop()
            return

        if action == CrawlerActions.DO_SKIP_TO_NEXT:
            self.queue.move(queue_item, QueueItem.STATUS_FINISHED)
            return

        if action == CrawlerActions.DO_CONTINUE_CRAWLING or action is None:
            self.queue.move(queue_item, QueueItem.STATUS_IN_PROGRESS)

            thread = CrawlerThread(self.__request_finish, self.__lock, self.__options, queue_item)
            thread.daemon = True
            thread.start()

    def __request_finish(self, queue_item, new_requests, new_queue_item_status=None):
        """Called when the crawler finished the given queued item.

        Args:
            queue_item (:class:`nyawc.QueueItem`): The request/response pair that finished.
            new_requests list(:class:`nyawc.http.Request`): All the requests that were found during this request.
            new_queue_item_status (str): The new status of the queue item (if it needs to be moved).

        """

        # Please note that the status may have changed to cancelled because the crawler was stopped.
        if queue_item.status == QueueItem.STATUS_CANCELLED:
            return

        new_queue_items = []
        action = None

        if new_queue_item_status:
            self.queue.move(queue_item, new_queue_item_status)

        if queue_item.status not in [QueueItem.STATUS_ERRORED, QueueItem.STATUS_CANCELLED]:
            for new_request in new_requests:
                HTTPRequestHelper.patch_with_options(new_request, self.__options, queue_item)

                if not HTTPRequestHelper.complies_with_scope(queue_item, new_request, self.__options.scope):
                    continue

                if self.queue.has_request(new_request):
                    continue

                new_request.depth = queue_item.request.depth + 1
                if self.__options.scope.max_depth is not None:
                    if new_request.depth > self.__options.scope.max_depth:
                        continue

                new_queue_item = self.queue.add_request(new_request)
                new_queue_items.append(new_queue_item)

            self.queue.move(queue_item, QueueItem.STATUS_FINISHED)
            action = self.__options.callbacks.request_after_finish(self.queue, queue_item, new_queue_items)

        if action == CrawlerActions.DO_STOP_CRAWLING:
            self.__crawler_stop()
            return

        if action == CrawlerActions.DO_CONTINUE_CRAWLING or action is None:
            self.__spawn_new_requests()
            return
