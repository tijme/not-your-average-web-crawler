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

from urllib.parse import urlparse

class HTTPRequestHelper:

    @staticmethod
    def patch_with_options(request, options):
        pass
        # ToDo: add options to request.
        # ToDo: by reference, no need to return.

    @staticmethod
    def is_already_in_queue(request, queue):
        # ToDo: check get/post request already in queue.
        # ToDo: strip trailing slashes etc.
        # ToDo: the check below is definetely not enough.

        for queue_item in queue.get_all():
            if queue_item.request.method == request.method:
                if queue_item.request.url == request.url:
                    return True

        return False

    @staticmethod
    def complies_with_scope(queue_item, new_request, scope):
        parsed_url = urlparse(queue_item.request.url)
        parsed_new_url = urlparse(new_request.url)

        subdomain = parsed_url.netloc.split(".")[:-2]
        subdomain_new = parsed_new_url.netloc.split(".")[:-2]

        if scope.protocol_must_match:
            if parsed_url.scheme != parsed_new_url.scheme:
                return False

        if scope.subdomain_must_match:
            if subdomain != subdomain_new:
                return False

        if scope.domain_must_match:
            if parsed_url.netloc != parsed_new_url.netloc:
                return False

        return True