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

class Response:
    """The Response class contains details that the request returned.

    Attributes:
        status (int): The HTTP response status.
        cookie (str): The cookie string that the server returned.
        content_type (str): The content type that the server returned.
        body (str): The response body (e.g. HTML or image data).
        __raw_body (str): The raw response body (not yet decoded).
        __raw_info (obj): The meta-information of the response, such as headers.
    """

    status = None

    cookie = None

    content_type = None

    body = None

    __raw_body = None

    __raw_info = None

    def fill(self, status, body, info):
        """Fill the Request class.

        Args:
            status (str): The HTTP response status code.
	        body (str): The response body (e.g. HTML or image data).
	        info (obj): The meta-information of the response, such as headers.
        """

        self.status = status
        self.body = body
        self.cookie = None # ToDo
        self.content_type = info.get_content_type()

        self.__raw_body = body
        self.__raw_info = info
