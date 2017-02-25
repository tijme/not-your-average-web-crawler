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

class Queue:
    """The Queue class contains all the request/response pairs that are going to be or have been crawled.

    Attributes:
        __items list(obj): The request/response pairs (as QueueItem's). 
    """

    __items = []

    def add(self, item):
        """Add a request/response pair (QueueItem) to the queue.

        Args:
            item (obj): The QueueItem to add.
        """

        self.__items.append(item)

    def add_request(self, request):
        """Add a request to the queue.

        Args:
            request (obj): The request to add.
        """

        self.add(QueueItem(request, Response()))

    def get_first(self, status):
        """Get the first item in the queue that has the given status.

        Args:
            status (str): return the first item with this status.
        """

        for item in self.__items:
            if item.status is status:
                return item

        return None

    def get_all(self):
        """Get all the items in the queue."""

        return self.__items

    def get_all_including(self, include):
        """Get all the items that contain atleast one of the given statuses.

        Args:
            include list(str): an array of statuses.
        """

        filtered_items = []

        for item in self.__items:
            if item.status in include:
                filtered_items.append(item)

        return filtered_items

    def get_all_excluding(self, exclude):
        """Get all the items that do not contain one of the given statuses.

        Args:
            exclude list(str): an array of statuses.
        """

        filtered_items = []

        for item in self.__items:
            if item.status not in exclude:
                filtered_items.append(item)

        return filtered_items

    def get_count(self):
        """Get a count of all the items in the queue."""

        return len(self.__items)

    def get_count_including(self, include):
        """Get a count of the items that contain atleast one of the given statuses.

        Args:
            include list(str): an array of statuses.
        """

        count = 0

        for item in self.__items:
            if item.status in include:
                count += 1

        return count

    def get_count_excluding(self, exclude):
        """Get a count of the items that do not contain one of the given statuses.

        Args:
            exclude list(str): an array of statuses.
        """

        count = 0

        for item in self.__items:
            if item.status not in exclude:
                count += 1

        return count

class QueueItem:
    """The QueueItem class keeps track of the request, response and the crawling status.

    Attributes:
        STATUS_QUEUED (str): Status for when the crawler did not yet start the request.
        STATUS_IN_PROGRESS (str): Status for when the crawler is currently crawling the request.
        STATUS_FINISHED (str): Status for when the crawler has finished crawling the request.
        STATUS_CANCELLED (str): Status for when the crawler has cancelled the request.
        status (str): The current crawling status.
        request (obj): The Request object.
        response (obj): The Response object.
    """

    STATUS_QUEUED = "queued"

    STATUS_IN_PROGRESS = "in_progress"

    STATUS_FINISHED = "finished"

    STATUS_CANCELLED = "cancelled"

    status = STATUS_QUEUED

    request = None

    response = None

    def __init__(self, request, response):
        """Constructs a QueueItem class.

        Args:
            request (obj): The Request object.
            response (obj): The Response object (empty object when initialized).
        """
        self.request = request
        self.response = response