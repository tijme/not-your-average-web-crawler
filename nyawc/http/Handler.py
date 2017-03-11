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
import importlib
import os

class Handler:
    """The Handler class executes HTTP requests.

    Attributes:
        __queue_item (obj): The queue item containing a request to execute.

    """

    __queue_item = None

    def __init__(self, queue_item):
        """Construct the HTTP handler.

        Args:
            queue_item (obj): The queue item containing the request.

        """

        self.__queue_item = queue_item

        self.__queue_item.response = self.__make_request(
            self.__queue_item.request.url,
            self.__queue_item.request.method,
            self.__queue_item.request.data,
            self.__queue_item.request.cookies,
            {
                'User-Agent': self.__queue_item.request.user_agent
            }
        )

    def get_new_requests(self):
        """Retrieve all the new request that were found in this request.

        Returns:
            list(obj): A list of request objects.

        """

        content_type = self.__queue_item.response.headers.get('content-type')
        scrapers = self.__get_all_scrapers()
        requests = []

        for scraper in scrapers:
            instance = scraper(self.__queue_item)
            if self.__content_type_matches(content_type, instance.content_types):
                requests.extend(instance.get_requests())

        return requests

    def __make_request(self, url, method, data, cookies, headers):
        """Execute a request with the given data.

        Args:
            url (str): The URL to call.
            method (str): The method (e.g. `get` or `post`).
            data (str): The data to call the URL with.
            cookies (obj): The cookie dict.
            headers (obj): The header dict.

        Returns:
            obj: The response object.

        """

        request_by_method = getattr(requests, method)
        return request_by_method(
            url=url, 
            data=data, 
            cookies=cookies, 
            headers=headers,
            allow_redirects=True,
            stream=True
        )

    def __get_all_scrapers(self):
        """Find all available scraper references.

        Returns:
            list(obj): The scraper references.

        """

        modules_strings = self.__get_all_scrapers_modules()
        modules = []

        for module_string in modules_strings:
            module = importlib.import_module("nyawc.scrapers." + module_string)
            modules.append(getattr(module, module_string))

        return modules

    def __get_all_scrapers_modules(self):
        """Find all available scraper modules.

        Returns:
            list(obj): The scraper modules.

        """

        modules = []
        
        file = os.path.realpath(__file__)
        folder = os.path.dirname(file)

        for filename in os.listdir(folder + "/../scrapers"):
            if filename.endswith("Scraper.py"):
                modules.append(filename[:-3])

        return modules

    def __content_type_matches(self, content_type, available_content_types):
        """Check if the given content type matches one of the available content types.

        Args:
            content_type (str): The given content type.
            available_content_types list(str): All the available content types.

        Returns:
            bool: True if a match was found, False otherwise.

        """

        if content_type is None:
            return False

        if content_type in available_content_types:
            return True

        for available_content_type in available_content_types:
            if available_content_type in content_type:
                return True

        return False