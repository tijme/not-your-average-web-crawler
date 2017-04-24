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
from nyawc.http.Response import Response
from nyawc.QueueItem import QueueItem
from nyawc.helpers.URLHelper import URLHelper
from nyawc.helpers.CookieHelper import CookieHelper
from collections import OrderedDict

import sys

class Queue:

    __options = None

    count_total = 0

    count_queued = 0

    count_in_progress = 0

    count_finished = 0

    count_cancelled = 0

    count_errored = 0

    items_queued = OrderedDict()

    items_in_progress = OrderedDict()

    items_finished = OrderedDict()

    items_cancelled = OrderedDict()

    items_errored = OrderedDict()

    def __init__(self, options):
        self.__options = options

    def add_request(self, request):
        queue_item = QueueItem(request, Response())
        self.add(queue_item)
        return queue_item

    def has_request(self, request):
        queue_item = QueueItem(request, Response())
        key = self.__get_key(queue_item)

        for status in QueueItem.STATUSES:
            if key in getattr(self, "items_" + status).keys():
                return True

        return False

    def add(self, queue_item):
        items = getattr(self, "items_" + queue_item.status)
        items_count = getattr(self, "count_" + queue_item.status)

        items[self.__get_key(queue_item)] = queue_item
        items_count += 1

        print("NEW COUNT {}: ".format(queue_item.status) + str(getattr(self, "count_" + queue_item.status)))

        self.count_total += 1

    def move(self, queue_item, status):
        items = getattr(self, "items_" + queue_item.status)
        count = getattr(self, "count_" + queue_item.status)

        del items[self.__get_key(queue_item)]
        count -= 1

        queue_item.status = status
        self.add(queue_item)

    def get_first(self, status):
        items = self.get_all(status)

        if len(items) > 0:
            return list(items.items())[0][1]

        return None

    def get_all(self, status):
        return getattr(self, "items_" + status)

    def get_progress(self):
        count_remaining = self.count_queued + self.count_in_progress
        percentage_remaining = 100 / self.count_total * count_remaining

        return 100 - percentage_remaining

    def __get_key(self, queue_item):
        key = queue_item.request.method

        if self.__options.scope.protocol_must_match:
            key += URLHelper.get_protocol(queue_item.request.url)

        if self.__options.scope.subdomain_must_match:
            key += URLHelper.get_subdomain(queue_item.request.url)

        key += URLHelper.get_domain(queue_item.request.url)
        key += str(URLHelper.get_ordered_params(queue_item.request.url))
        key += str(CookieHelper.get_ordered_cookies(queue_item.request.cookies))

        return key