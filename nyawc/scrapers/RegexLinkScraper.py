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

from nyawc.http.Request import Request
from nyawc.helpers.URLHelper import URLHelper

import re

class RegexLinkScraper:
    """The RegexLinkScraper finds absolute URLs between quotes.

    Attributes:
        content_types list(str): The supported content types.
        __expressions list(obj): The queue item containing the response to scrape.
        __queue_item (obj): The queue item containing the response to scrape.

    """

    content_types = [
        "text/html"
    ]

    __expressions = [
        # Match absolute/relative URLs between any type of HTML quote
        { "group": 4, "raw": r"((src|link|href|url)(\=))([\"\'\`])(((((https?:)?\/)?\/)|(\.\.\/)+)([^\s]*?))\4" },
    ]

    __queue_item = None

    def __init__(self, queue_item):
        """Construct the RegexLinkScraper class.

        Args:
            queue_item (obj): The queue item containing a response the scrape.

        """

        self.__queue_item = queue_item

    def get_requests(self):
        """Get all the new requests that were found in the response.

        Returns:
            list(obj): A list of new requests.

        """

        host = self.__queue_item.request.url
        content = self.__queue_item.response.text

        return self.get_requests_from_content(host, content)

    def get_requests_from_content(self, host, content):
        """Find new requests from the given content.

        Args:
            host (str): The parent request URL.
            content (obj): The HTML content.

        Returns:
            list(obj): Requests that were found.

        """

        found_requests = []

        for expression in self.__expressions:
            matches = re.findall(expression["raw"], content)

            for match in matches:
                found_url = match[expression["group"]]
                absolute_url = URLHelper.make_absolute(host, found_url)
                found_requests.append(Request(absolute_url))

        return found_requests