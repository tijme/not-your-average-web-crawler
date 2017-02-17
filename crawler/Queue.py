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

    def __is_unique(self, request):
        is_unique = True

        for existing_request in self.__requests:
            if self.__does_url_match(request, existing_request):
                is_unique = False
                break

            # TODO: Add more matches here!

        return is_unique

    def __does_url_match(self, req1, req2):
        url1 = req1.req_url
        url2 = req2.req_url

        if url1.endswith("/"):
            url1 = url1[:-1]

        if url2.endswith("/"):
            url2 = url2[:-1]

        return url1 == url2