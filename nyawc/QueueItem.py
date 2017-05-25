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

from bs4 import BeautifulSoup

class QueueItem:
    """The QueueItem class keeps track of the request and response and the crawling status.

    Attributes:
        STATUS_QUEUED (str): Status for when the crawler did not yet start the request.
        STATUS_IN_PROGRESS (str): Status for when the crawler is currently crawling the request.
        STATUS_FINISHED (str): Status for when the crawler has finished crawling the request.
        STATUS_CANCELLED (str): Status for when the crawler has cancelled the request.
        STATUS_ERRORED (str): Status for when the crawler could not execute the request.
        STATUSES (arr): All statuses.
        status (str): The current crawling status.
        request (:class:`nyawc.http.Request`): The Request object.
        response (:class:`nyawc.http.Response`): The Response object.
        response_soup (obj): The BeautifulSoup container for the response text.

    """

    STATUS_QUEUED = "queued"

    STATUS_IN_PROGRESS = "in_progress"

    STATUS_FINISHED = "finished"

    STATUS_CANCELLED = "cancelled"

    STATUS_ERRORED = "errored"

    STATUSES = [
        STATUS_QUEUED,
        STATUS_IN_PROGRESS,
        STATUS_FINISHED,
        STATUS_CANCELLED,
        STATUS_ERRORED
    ]

    def __init__(self, request, response):
        """Constructs a QueueItem instance.

        Args:
            request (:class:`nyawc.http.Request`): The Request object.
            response (:class:`nyawc.http.Response`): The Response object (empty object when initialized).

        """

        self.status = QueueItem.STATUS_QUEUED
        self.response_soup = None

        self.request = request
        self.response = response

    def get_soup_response(self):
        """Get the response as a cached BeautifulSoup container.

        Returns:
            obj: The BeautifulSoup container.

        """

        if self.response is not None:
            if self.response_soup is None:
                self.response_soup = BeautifulSoup(self.response.text, "lxml")

        return self.response_soup
