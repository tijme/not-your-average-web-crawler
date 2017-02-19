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

from src.Crawler import Crawler
from src.Request import Request
from src.helpers.LinkHelper import LinkHelper
from bs4 import BeautifulSoup
import html5lib

"""

"""
class SoupLinkFinder:

    def __init__(self, host, content):
        self.__host = host
        self.__soup = BeautifulSoup(content, "html5lib")

    def get_requests(self):
        found_requests = []


        for link in self.__soup.find_all("a", href=True):
            href = self.trim_grave_accent(link["href"])
            absolute_link = LinkHelper.get_instance().make_absolute(self.__host, href)
            new_request = Request(absolute_link, Request.METHOD_GET)
            found_requests.append(new_request)

        return found_requests

    def trim_grave_accent(self, href):
        if href.startswith("`"):
            href = href[1:]

        if href.endswith("`"):
            href = href[:-1]

        return href