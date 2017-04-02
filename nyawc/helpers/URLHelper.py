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

        query = OrderedDict(parse_qsl(url_parts[4]))
        query.update(data)

        url_parts[4] = urlencode(query)

        return urlunparse(url_parts)

    @staticmethod
    def are_urls_similar(url1, url2):
        """Check if the given URLs are similar to each other.

        Args:
            url1 (str): The first URL.
            url2 (str): The second URL.

        Returns:
            bool: True if similar, False otherwise.

        """

        parsed_url1 = urlparse(url1)
        parsed_url2 = urlparse(url2)

        if parsed_url1.netloc != parsed_url2.netloc:
            return False

        if parsed_url1.path != parsed_url2.path:
            return False

        dict_url1 = dict(parse_qsl(parsed_url1.query))
        dict_url2 = dict(parse_qsl(parsed_url2.query))

        return URLHelper.is_data_similar(dict_url1, dict_url2)

    @staticmethod
    def is_data_similar(data1, data2):
        """Check if the given data dicts are similar to each other.

        Args:
            data1 (obj): The first data object.
            data2 (obj): The second data object.

        Returns:
            bool: True if similar, False otherwise.

        """

        if data1 is None and data2 is not None:
            return False

        if data2 is None and data1 is not None:
            return False

        if data1 is None and data2 is None:
            return True

        return data1.keys() == data2.keys()

    @staticmethod
    def is_mailto(url):
        """Check if the given URL is a mailto URL

        Args:
            url (str): The URL to check.

        Returns:
            bool: True if mailto, False otherwise.

        """

        return url.startswith("mailto:")