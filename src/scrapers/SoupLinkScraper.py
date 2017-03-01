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
import html5lib

class SoupLinkScraper:

    __content_types = [
        "text/html"
    ]

    __queue_item = None

    def __init__(self, queue_item):
        self.__queue_item = queue_item

    def get_requests(self):
        content_type = self.__queue_item.response.headers.get('content-type')

        if not self.__content_type_matches(content_type):
            return []

        host = self.__queue_item.request.url
        soup = BeautifulSoup(self.__queue_item.response.text, "html5lib")
        links = soup.find_all("a", href=True)

        found_requests = []

        for link in links:
            found_url = self.trim_grave_accent(link["href"])
            absolute_url = URLHelper.make_absolute(host, found_url)
            found_requests.append(Request(absolute_url))

        return found_requests

    def trim_grave_accent(self, href):
        if href.startswith("`"):
            href = href[1:]

        if href.endswith("`"):
            href = href[:-1]

        return href

    def __content_type_matches(self, content_type):
        if content_type in self.__content_types:
            return True

        for available_content_type in self.__content_types:
            if available_content_type in content_type:
                return True

        return False