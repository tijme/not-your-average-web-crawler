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

from src.http.Request import Request
from src.helpers.URLHelper import URLHelper
from bs4 import BeautifulSoup

import re

class RegexLinkScraper:

    __content_types = [
        "text/html",
        "text/css",
        "text/javascript"
    ]

    __expressions = [
        # Match absolute/relative URLs between any type of HTML quote
        { "group": 1, "raw": r"([\"\'\`])(((((https?:)?\/)?\/)|(\.\.\/)+)(.*?))\1" },

        # Match all absolute URLs outside of HTML quotes
        { "group": 1, "raw": r"([^\"\'\`])((https?:\/\/)([^\s\"\'\`]*))" }
    ]

    __queue_item = None

    def __init__(self, queue_item):
        self.__queue_item = queue_item

    def get_requests(self):
        content_type = self.__queue_item.response.headers.get('content-type')

        if not self.__content_type_matches(content_type):
            return []

        host = self.__queue_item.request.url
        content = self.__queue_item.response.text

        return self.get_requests_from_content(host, content)

    def get_requests_from_content(self, host, content):
        found_requests = []

        for expression in self.__expressions:
            matches = re.findall(expression["raw"], content)

            for match in matches:
                found_url = match[expression["group"]]
                absolute_url = URLHelper.make_absolute(host, found_url)
                found_requests.append(Request(absolute_url))

        return found_requests

    def __content_type_matches(self, content_type):
        if content_type in self.__content_types:
            return True

        for available_content_type in self.__content_types:
            if available_content_type in content_type:
                return True

        return False