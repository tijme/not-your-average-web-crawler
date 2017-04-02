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

from nyawc.helpers.URLHelper import URLHelper
from nyawc.helpers.CookieHelper import CookieHelper

class Request:
    """The Request class contains details that were used to request the specified URL.

    Attributes:
        REQUEST_METHOD_OPTIONS (str): A request method that can be used to request the URL.
        REQUEST_METHOD_GET (str): A request method that can be used to request the URL.
        REQUEST_METHOD_HEAD (str): A request method that can be used to request the URL.
        REQUEST_METHOD_POST (str): A request method that can be used to request the URL.
        REQUEST_METHOD_PUT (str): A request method that can be used to request the URL.
        REQUEST_METHOD_DELETE (str): A request method that can be used to request the URL.
        REQUEST_METHODS list(str): All available request methods in a list.
        parent_raised_error (bool): If the parent request raised an error (e.g. 404).
        depth (int): The current crawling depth.
        url (str): The absolute URL to use when making the request.
        method (str): The request method to use for the request.
        data (obj): The post data {key: value} OrderedDict that will be sent.
        cookies (obj): The (requests module) cookie jar to use for the request.
        user_agent (str): The user agent to use for the request.

    """

    METHOD_OPTIONS = "options"

    METHOD_GET = "get"

    METHOD_HEAD = "head"

    METHOD_POST = "post"

    METHOD_PUT = "put"

    METHOD_DELETE = "delete"

    METHODS = [
        METHOD_OPTIONS,
        METHOD_GET,
        METHOD_HEAD,
        METHOD_POST,
        METHOD_PUT,
        METHOD_DELETE
    ]

    parent_raised_error = False

    depth = 0

    url = None

    method = None

    data = None

    cookies = None

    user_agent = None

    def __init__(self, url, method=METHOD_GET, data=None, cookies=None, user_agent=None):
        """Constructs a Request class.

        Args:
            url (str): The absolute URL to use when making the request.
            method (str): The request method to use for the request.
            data (obj): The post data {key: value} OrderedDict that will be sent.
            cookies (obj): The (requests module) cookie jar to use for the request.
            user_agent (str): The user agent to use for the request.

        """

        self.url = url
        self.method = method
        self.cookies = cookies
        self.user_agent = user_agent

        if method == self.METHOD_GET:
            self.url = URLHelper.append_with_data(self.url, data)
            self.data = None
        else:
            self.data = data

    def is_same_as(self, request):
        """Check if this request is the same to the given request.

        Args:
            request (obj): Check if self is the same as this request.

        Returns:
            bool: True if the same, False otherwise.

        """

        if self.url != request.url:
            return False

        if self.method != request.method:
            return False

        if not CookieHelper.are_cookies_the_same(self.cookies, request.cookies):
            return False

        return True

    def is_similar_to(self, request):
        """Check if this request is similar to the given request.

        Args:
            request (obj): Check if self is similar as this request.

        Returns:
            bool: True if similar, False otherwise.

        """

        if self.method != request.method:
            return False

        if not URLHelper.is_data_similar(self.data, request.data):
            return False

        if not CookieHelper.are_cookies_similar(self.cookies, request.cookies):
            return False

        if self.url != request.url:
            if not URLHelper.are_urls_similar(self.url, request.url):
                return False

        return True