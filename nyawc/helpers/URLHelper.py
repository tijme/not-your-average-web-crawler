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

from urllib.parse import urljoin, urlparse, parse_qsl, urlencode, urlunparse
from collections import OrderedDict

class URLHelper:
    """A helper for URL strings."""

    @staticmethod
    def make_absolute(parent_absolute, relative):
        """Make the given (relative) URL absolute.

        Args:
            parent_absolute (str): The absolute URL the relative url was found on.
            relative (str): The (possibly relative) url to make absolute.

        Returns:
            str: The absolute URL.

        """

        # Python 3.4 and lower do not remove folder traversal strings.
        # This was fixed in 3.5 (https://docs.python.org/3/whatsnew/3.5.html#urllib)
        while(relative.startswith('/../') or relative.startswith('../')):
            relative = relative[3:]

        return urljoin(parent_absolute, relative)

    @staticmethod
    def append_with_data(url, data):
        """Append the given URL with the given data OrderedDict.

        Args:
            url (str): The URL to append.
            data (obj): The key value OrderedDict to append to the URL.

        Returns:
            str: The new URL.

        """

        if data is None:
            return url

        url_parts = list(urlparse(url))

        query = OrderedDict(parse_qsl(url_parts[4], keep_blank_values=True))
        query.update(data)

        url_parts[4] = urlencode(query)

        return urlunparse(url_parts)

    @staticmethod
    def is_mailto(url):
        """Check if the given URL is a mailto URL

        Args:
            url (str): The URL to check.

        Returns:
            bool: True if mailto, False otherwise.

        """

        return url.startswith("mailto:")

    @staticmethod
    def get_protocol(url):
        parsed_url = urlparse(url)
        return parsed_url.scheme

    @staticmethod
    def get_subdomain(url):
        parsed_url = urlparse(url)
        return ".".join(parsed_url.netloc.split(".")[:-2])

    @staticmethod
    def get_domain(url):
        parsed_url = urlparse(url)
        return ".".join(parsed_url.netloc.split(".")[-2:])

    @staticmethod
    def get_ordered_params(url):
        parsed_url = urlparse(url)
        params = dict(parse_qsl(parsed_url.query, keep_blank_values=True))
        return OrderedDict(sorted(params.items()))