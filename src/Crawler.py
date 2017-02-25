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

from src.Queue import Queue, QueueItem
from src.http.Handler import Handler
from src.http.Request import Request
from src.helpers.HTTPRequestHelper import HTTPRequestHelper
from src.helpers.HTTPResponseHelper import HTTPResponseHelper

class Crawler:
    """The main Crawler class which handles the crawling recursion, queue and processes.

    Attributes:
        __options (obj): The options to use for the current crawling runtime.
        __queue (obj): The request/response pair queue containing everything to crawl.
    """

    __options = None

    __queue = Queue()

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
        while concurrent_requests_count < self.__options.performance.max_processes:
            self.__spawn_new_request()
            concurrent_requests_count += 1

    def __spawn_new_request(self):
        """Spawn the first queued request if available."""

        first_in_line = self.__queue.get_first(QueueItem.STATUS_QUEUED)
        if first_in_line is not None:
            self.__request_start(first_in_line)

    def __crawler_start(self):
        """Spawn the first X queued request, where X is the max processes option."""

        self.__options.callbacks.crawler_before_start()
        self.__spawn_new_requests()

    def __crawler_stop(self):
        """Spawn the first X queued request, where X is the max processes option."""

        # ToDo: stop all active processes
        # ToDo: set flag so that no new processes will be spawned
        self.__crawler_finish()

    def __crawler_finish(self):
        """Called when the crawler is finished because there are no queued requests left or it was stopped."""

        self.__options.callbacks.crawler_after_finish(self.__queue)

    def __request_start(self, queue_item):
        """Execute the request in given queue item.

        Args:
            queue_item (obj): The request/response pair to scrape.
        """

        action = self.__options.callbacks.request_before_start(queue_item)

        if action == CrawlerActions.DO_STOP_CRAWLING:
            return self.__crawler_stop()

        if action == CrawlerActions.DO_SKIP_TO_NEXT:
            queue_item.status = QueueItem.STATUS_FINISHED
            return None

        if action == CrawlerActions.DO_CONTINUE_CRAWLING or action is None:
            queue_item.status = QueueItem.STATUS_IN_PROGRESS

            handler = Handler(queue_item)
            new_requests = handler.get_new_requests()
            new_queue_items = []
            
            for new_request in new_requests:
                if HTTPRequestHelper.is_already_in_queue(new_request, self.__queue):
                    continue

                HTTPRequestHelper.patch_with_options(request, self.__options)
                self.__queue.add_request(request)
                new_queue_items.append(request)
                
            self.__request_finish(queue_item, new_queue_items)

    def __request_finish(self, queue_item, new_queue_items):
        """Called when the crawler finished the given queued item.

        Args:
            queue_item (obj): The request/response pair that finished.
            new_queue_items list(obj): All the request/response pairs that were found during this request.
        """

        queue_item.status = QueueItem.STATUS_FINISHED
        action = self.__options.callbacks.request_after_finish(queue_item, new_queue_items)

        if action == CrawlerActions.DO_STOP_CRAWLING:
            return self.__crawler_stop()

        if action == CrawlerActions.DO_CONTINUE_CRAWLING or action is None:
            return self.__spawn_new_requests()

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