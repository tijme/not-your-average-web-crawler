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
from src.Scraper import Scraper
from src.http.Handler import Handler
from src.http.Request import Request
from src.http.Response import Response
from src.helpers import HTTPRequestHelper
from src.helpers import HTTPResponseHelper

class Crawler:

    __options = None

    __queue = Queue()

    def __init__(self, options):
        self.__options = options

    def start_with(self, request):
        patched_request = HTTPRequestHelper.patch_with_options(request, self.__options)
        queue_item = QueueItem(patched_request, Response())
        self.__queue.add(queue_item)
        self.__crawler_start()

    def __spawn_new_requests():
        concurrent_requests_count = self.__queue.get_count_including([QueueItem.STATUS_IN_PROGRESS])
        while concurrent_requests_count < self.__options.performance.max_processes:
            self.__spawn_new_request()
            concurrent_requests_count += 1

    def __spawn_new_request():
        first_in_line = self.__queue.get_first(QueueItem.STATUS_QUEUED)
        self.__request_start(first_in_line)

    def __crawler_start():
        self.__options.callbacks.crawler_before_start()

    def __crawler_stop():
        # ToDo: stop all active processes
        # ToDo: set flag so that no new processes will be spawned
        self.__crawler_finish()

    def __crawler_finish():
        self.__options.callbacks.crawler_after_finish()

    def __request_start(queue_item):
        action = self.__options.callback.request_before_start()

        if action == CrawlerActions.DO_STOP_CRAWLING:
            return self.__crawler_stop()

        if action == CrawlerActions.DO_SKIP_TO_NEXT:
            return None

        if action == CrawlerActions.DO_CONTINUE_CRAWLING:
            handler = Handler(queue_item)
            new_requests = handler.get_new_requests()
            
            for new_request in new_requests:
                if HTTPRequestHelper.is_already_in_queue(new_request, self.__queue):
                    continue

                patched_request = HTTPRequestHelper.patch_with_options(request, self.__options)
                queue_item = QueueItem(patched_request, Response())
                self.__queue.add(queue_item)

            self.__request_finish(queue_item)

    def __request_finish(queue_item):
        action = self.__options.callbacks.cb_crawler_after_finish()

        if action == CrawlerActions.DO_STOP_CRAWLING:
            return self.__crawler_stop()

        if action == CrawlerActions.DO_CONTINUE_CRAWLING:
            return self.__spawn_new_requests()

class CrawlerActions:

    DO_CONTINUE_CRAWLING = 1

    DO_SKIP_TO_NEXT = 2

    DO_STOP_CRAWLING = 3