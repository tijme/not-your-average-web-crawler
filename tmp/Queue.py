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

from src.helpers.LinkHelper import LinkHelper

"""

"""
class Queue:

    __requests = []

    def add(self, request):
        if self.__is_unique(request):
            self.__requests.append(request)
        
    def get_first(self, status=None):
        for request in self.__requests:
            if status is not None and request.status is not status:
                continue

            return request

        return None

    def get_all(self, status=None):
        results = []

        for request in self.__requests:
            if status is not None and request.status is status:
                results.append(request)

        return results

    def get_count(self, status=None):
        if status is None:
            return len(self.__requests)

        count = 0

        for request in self.__requests:
            if request.status is status:
                count += 1

        return count

    def get_count_without(self, status):
        count = 0

        for request in self.__requests:
            if request.status is not status:
                count += 1

        return count

    def __is_unique(self, request):
        is_unique = True

        for existing_request in self.__requests:
            if LinkHelper.get_instance().does_url_match(request, existing_request):
                is_unique = False
                break

            # TODO: Add more matches here!

        return is_unique