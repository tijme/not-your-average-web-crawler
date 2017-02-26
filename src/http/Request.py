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
        url (str): The absolute URL to use when making the request.
        method (str): The request method to use for the request.
        cookie (obj): The cookies {key: value} object to use for the request.
        user_agent (str): The user agent to use for the request.
        data (obj): The post data {key: value} object that will be sent.
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

    url = None

    method = None

    data = None

    cookie = None

    user_agent = None

    def __init__(self, url, method=METHOD_GET, data=None, cookie=None, user_agent=None):
        """Constructs a Request class.

        Args:
            url (str): The absolute URL to use when making the request.
            method (str): The request method to use for the request.
            cookie (obj): The cookies {key: value} object to use for the request.
            user_agent (str): The user agent to use for the request.
            data (obj): The post data {key: value} object that will be sent.
        """

        self.url = url
        self.method = method
        self.data = data
        self.cookie = cookie
        self.user_agent = user_agent