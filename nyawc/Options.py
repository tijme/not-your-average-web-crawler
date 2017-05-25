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

import requests

from nyawc.CrawlerActions import CrawlerActions

class Options:
    """The Options class contains all the crawling settings/options.

    Attributes:
        scope (:class:`nyawc.Options.OptionsScope`): Can be used to define the crawling scope.
        callbacks (:class:`nyawc.Options.OptionsCallbacks`): Can be used to define crawling callbacks.
        performance (:class:`nyawc.Options.OptionsPerformance`): Can be used to define performance options.
        identity (:class:`nyawc.Options.OptionsIdentity`): Can be used to define the identity/footprint options.

    """

    def __init__(self):
        """Constructs an Options instance."""

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
        max_depth (obj): the maximum search depth. For example, 2 would be the startpoint and all the pages found on it. Default is None (unlimited).

    """

    def __init__(self):
        """Constructs an OptionsScope instance."""

        self.protocol_must_match = False
        self.subdomain_must_match = True
        self.domain_must_match = True
        self.max_depth = None

class OptionsCallbacks:
    """The OptionsCallbacks class contains all the callback methods.

    Attributes:
        crawler_before_start (obj): called before the crawler starts crawling. Default is a null route to :attr:`__null_route_crawler_before_start`.
        crawler_after_finish (obj): called after the crawler finished crawling. Default is a null route to :attr:`__null_route_crawler_after_finish`.
        request_before_start (obj): called before the crawler starts a new request. Default is a null route to :attr:`__null_route_request_before_start`.
        request_after_finish (obj): called after the crawler finishes a request. Default is a null route to :attr:`__null_route_request_after_finish`.
        form_before_autofill (obj): called before the crawler starts autofilling a form. Default is a null route to :attr:`__null_route_form_before_autofill`.
        form_after_autofill (obj): called after the crawler finishes autofilling a form. Default is a null route to :attr:`__null_route_form_after_autofill`.

    """

    def __init__(self):
        """Constructs an OptionsCallbacks instance."""

        self.crawler_before_start = self.__null_route_crawler_before_start
        self.crawler_after_finish = self.__null_route_crawler_after_finish
        self.request_before_start = self.__null_route_request_before_start
        self.request_after_finish = self.__null_route_request_after_finish
        self.form_before_autofill = self.__null_route_form_before_autofill
        self.form_after_autofill = self.__null_route_form_after_autofill

    def __null_route_crawler_before_start(self):
        """A null route for the 'crawler before start' callback."""

        pass

    def __null_route_crawler_after_finish(self, queue):
        """A null route for the 'crawler after finish' callback.

        Args:
            queue (obj): The current crawling queue.

        """

        pass

    def __null_route_request_before_start(self, queue, queue_item):
        """A null route for the 'request before start' callback.

        Args:
            queue (:class:`nyawc.Queue`): The current crawling queue.
            queue_item (:class:`nyawc.QueueItem`): The queue item that's about to start.

        Returns:
            str: A crawler action (either DO_SKIP_TO_NEXT, DO_STOP_CRAWLING or DO_CONTINUE_CRAWLING).

        """

        return CrawlerActions.DO_CONTINUE_CRAWLING

    def __null_route_request_after_finish(self, queue, queue_item, new_queue_items):
        """A null route for the 'request after finish' callback.

        Args:
            queue (:class:`nyawc.Queue`): The current crawling queue.
            queue_item (:class:`nyawc.QueueItem`): The queue item that was finished.
            new_queue_items list(:class:`nyawc.QueueItem`): The new queue items that were found in the one that finished.

        Returns:
            str: A crawler action (either DO_STOP_CRAWLING or DO_CONTINUE_CRAWLING).

        """

        return CrawlerActions.DO_CONTINUE_CRAWLING

    def __null_route_form_before_autofill(self, queue_item, elements, form_data):
        """A null route for the 'form before autofill' callback.

        Args:
            queue_item (:class:`nyawc.QueueItem`): The queue item that was finished.
            elements list(obj): The soup elements found in the form.
            form_data (obj): The {key: value} form fields to be autofilled.

        Returns:
            str: A crawler action (either DO_AUTOFILL_FORM or DO_NOT_AUTOFILL_FORM).

        """

        return CrawlerActions.DO_AUTOFILL_FORM

    def __null_route_form_after_autofill(self, queue_item, elements, form_data):
        """A null route for the 'form after autofill' callback.

        Args:
            queue_item (:class:`nyawc.QueueItem`): The queue item that was finished.
            elements list(obj): The soup elements found in the form.
            form_data (obj): The {key: value} form fields.

        """

        pass

class OptionsPerformance:
    """The OptionsPerformance class contains the performance settings/options.

    Attributes:
        max_threads (obj): the maximum amount of simultaneous threads to use for crawling.

    """

    def __init__(self):
        """Constructs an OptionsPerformance instance."""

        self.max_threads = 8

class OptionsIdentity:
    """The OptionsIdentity class contains the identity/footprint settings/options.

    Attributes:
        cookies (obj): The (requests module) cookie jar to use when making a request. For more information check http://docs.python-requests.org/en/master/user/quickstart/#cookies.
        headers (obj): The headers {key: value} to use when making a request.

    """

    def __init__(self):
        """Constructs an OptionsIdentity instance."""

        self.cookies = requests.cookies.RequestsCookieJar()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
        }
