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

import urllib.request
import importlib

"""

"""
class Request:

    STATUS_QUEUED = "queued"

    STATUS_IN_PROGRESS = "in_progress"

    STATUS_DONE = "done"

    STATUS_INVALID_CONTENT_TYPE = "invalid_content_type"

    STATUS_GET_ADDRESS_INFO_FAILED = "get_address_info_failed"

    METHOD_GET = "GET"

    METHOD_POST = "POST"

    METHOD_PUT = "PUT"

    METHOD_DELETE = "DELETE"

    status = None

    req_url = None

    req_method = None

    __finders = {
        "text/html": [
            "src.finders.SoupFormFinder:SoupFormFinder",
            "src.finders.SoupLinkFinder:SoupLinkFinder",
            "src.finders.RegexLinkFinder:RegexLinkFinder"
        ],
        "text/css": [
            "src.finders.RegexLinkFinder:RegexLinkFinder"
        ],
        "text/javascript": [
            "src.finders.RegexLinkFinder:RegexLinkFinder"
        ],
        "text/xml": [
            "src.finders.RegexLinkFinder:RegexLinkFinder"
        ],
        "application/xml": [
            "src.finders.RegexLinkFinder:RegexLinkFinder"
        ],
    }

    __found_requests = [
    ]

    def __init__(self, url, method):
        self.status = self.STATUS_QUEUED
        self.req_url = url
        self.req_method = method

    def execute(self):
        self.status = self.STATUS_IN_PROGRESS

        details = None
        content = None

        try:
            resource = urllib.request.urlopen(self.req_url)
            details = resource.info()
            content = resource.read()
        except urllib.error.HTTPError as error:
            details = error.fp.info()
            content = error.fp.read()
        except Exception:
            self.status = self.STATUS_GET_ADDRESS_INFO_FAILED
            return []

        finder_available = False
        for content_type, finders in self.__finders.items():
            for finder in finders:
                if content_type in details.get_content_type():
                    finder_available = True
                    self.__found_requests.extend(self.__run_finder(finder, content))

        if not finder_available:
            self.status = self.STATUS_INVALID_CONTENT_TYPE
            return []

        self.status = self.STATUS_DONE
        return self.__found_requests

    def __get_finder(self, name):
        components = name.split(':')
        module = importlib.import_module(components[0])
        return getattr(module, components[1])

    def __run_finder(self, finder, content):
        finder_class = self.__get_finder(finder)
        finder_instance = finder_class(self.req_url, content)
        return finder_instance.get_requests()
