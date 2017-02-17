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

from crawler.Queue import Queue
from crawler.Request import Request
from multiprocessing import Process
from urllib.parse import urlparse

"""

"""
class Crawler:

    cb_crawler_started = None

    cb_crawler_request_started = None

    cb_crawler_request_finished = None

    cb_crawler_finished = None

    opt_max_depth = float("inf")

    opt_max_processes = 8

    opt_domain_must_match = True

    __queue = Queue()

    def __init__(self, start_request=None):
        self.__queue.add(start_request)

    def start(self):
        self.__cb_crawler_started()

        request = self.__queue.get_first(Request.STATUS_QUEUED)
        self.__crawl_request(request)

    def __crawl_request(self, request):
        if request is None:
            self.__crawler_finished()
            return

        self.__crawler_request_started(request)

    def __crawler_request_started(self, request):
        do_continue = self.__cb_crawler_request_started(request)
        if not do_continue:
            self.__crawler_finished()
            return

        self.__crawler_request_execute(request)

    def __crawler_request_execute(self, request):
        new_requests = request.execute()
        self.__crawler_request_finished(request, new_requests)

    def __crawler_request_finished(self, request, new_requests):
        do_continue = self.__cb_crawler_request_finished(request, new_requests)
        if not do_continue:
            self.__crawler_finished()
            return

        for new_request in new_requests:
            if not self.opt_domain_must_match:
                self.__queue.add(new_request)
            elif self.__do_domains_match(request, new_request):
                self.__queue.add(new_request)

        request = self.__queue.get_first(Request.STATUS_QUEUED)
        if request is not None:
            self.__crawl_request(request)
        else:
            self.__crawler_finished()

    def __crawler_finished(self):
        self.__cb_crawler_finished()

    def __do_domains_match(self, req1, req2):
        parsed1 = urlparse(req1.req_url)
        parsed2 = urlparse(req2.req_url)
        return parsed1.netloc == parsed2.netloc

    """
    Callbacks........................
    """

    def __cb_crawler_started(self):
        if self.cb_crawler_started is not None:
            self.cb_crawler_started()

    def __cb_crawler_request_started(self, started_request):
        do_continue = True

        if self.cb_crawler_request_started is not None:
            do_continue = self.cb_crawler_request_started(started_request)

        return do_continue

    def __cb_crawler_request_finished(self, finished_request, new_requests):
        do_continue = True

        if self.cb_crawler_request_finished is not None:
            do_continue = self.cb_crawler_request_finished(finished_request, new_requests)

        return do_continue

    def __cb_crawler_finished(self):
        if self.cb_crawler_finished is not None:
            self.cb_crawler_finished(self.__queue.get_all(Request.STATUS_DONE))