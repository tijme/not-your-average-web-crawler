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

from nyawc.Crawler import CrawlerActions

import requests

class Options:
    """The Options class contains all the crawling settings/options.

    Attributes:
        scope (obj): Can be used to define the crawling scope.
        callbacks (obj): Can be used to define crawling callbacks.
        performance (obj): Can be used to define performance options.
        identity (obj): Can be used to define the identity/footprint options.

    """

    scope = None

    callbacks = None

    performance = None

    identity = None

    def __init__(self):
        """Constructs an Options class."""

        self.scope = OptionsScope()
        self.callbacks = OptionsCallbacks()
        self.performance = OptionsPerformance()
        self.identity = OptionsIdentity()

class OptionsScope:
    """The OptionsScope class contains the scope settings/options.

    Attributes:
        protocol_must_match (bool): only crawl pages with the same protocol as the startpoint (e.g. only https).
        subdomain_must_match (bool): only crawl pages with the same subdomain as the startpoint, if the startpoint is not a subdomain, no subdomains will be crawled.
        domain_must_match (bool): only crawl pages with the same domain as the startpoint (e.g. only finnwea.com).
        ignore_similar_requests (bool): ignore similar requests like `?page=1` & `?page=2` or `/page/1` and `/page/2`.
        max_depth (obj): the maximum search depth. For example, 2 would be the startpoint and all the pages found on it. Default is None (unlimited).

    """

    protocol_must_match = False

    subdomain_must_match = True

    domain_must_match = True

    ignore_similar_requests = False

    max_depth = None

class OptionsCallbacks:
    """The OptionsCallbacks class contains all the callback methods.

    Attributes:
        crawler_before_start (obj): called when the crawler starts crawling. Default is a null route.
        crawler_after_finish (obj): called when the crawler finished crawling. Default is a null route.
        request_before_start (obj): called when the crawler starts a new request. Default is a null route.
        request_after_finish (obj): called when the crawler finishes a request. Default is a null route.

    """

    crawler_before_start = None

    crawler_after_finish = None

    request_before_start = None

    request_after_finish = None

    def __init__(self):
        """Constructs an OptionsCallbacks class."""

        self.crawler_before_start = self.__null_route_crawler_before_start
        self.crawler_after_finish = self.__null_route_crawler_after_finish
        self.request_before_start = self.__null_route_request_before_start
        self.request_after_finish = self.__null_route_request_after_finish

    def __null_route_crawler_before_start(self):
        """A null route for the 'crawler before start' callback."""

        pass

    def __null_route_crawler_after_finish(self, queue):
        """A null route for the 'crawler after finish' callback.

        Args:
            queue (obj): The current crawling queue.

        """

        pass

    def __null_route_request_before_start(self, queue_item):
        """A null route for the 'request before start' callback.

        Args:
            queue_item (obj): The queue item that's about to start.

        Returns:
            str: A crawler action (either DO_SKIP_TO_NEXT, DO_STOP_CRAWLING or DO_CONTINUE_CRAWLING).

        """

        return CrawlerActions.DO_CONTINUE_CRAWLING

    def __null_route_request_after_finish(self, queue_item, new_queue_items):
        """A null route for the 'request after finish' callback.

        Args:
            queue_item (obj): The queue item that was finished.
            new_queue_items (obj): The new queue items that were found in the one that finished.

        Returns:
            str: A crawler action (either DO_STOP_CRAWLING or DO_CONTINUE_CRAWLING).

        """

        return CrawlerActions.DO_CONTINUE_CRAWLING

class OptionsPerformance:
    """The OptionsPerformance class contains the performance settings/options.

    Attributes:
        max_threads (obj): the maximum amount of simultaneous threads to use for crawling.
        
    """

    max_threads = 4

class OptionsIdentity:
    """The OptionsIdentity class contains the identity/footprint settings/options.

    Attributes:
        user_agent (str): the user agent to use when making a request.
        cookies (obj): the cookies to use when making a request.
        
    """

    # ToDo: Default this string to a random user agent
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"

    cookies = requests.cookies.RequestsCookieJar()