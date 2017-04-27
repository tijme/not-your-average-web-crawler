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

from nyawc.helpers.HTTPRequestHelper import HTTPRequestHelper
from nyawc.Queue import Queue
from nyawc.http.Request import Request
from nyawc.Options import Options

import unittest
 
class TestQueue(unittest.TestCase):
    """The TestQueue tests if the hashes and counters of the queue work correctly."""

    def test_hash_is_always_the_same(self):
        """Ensure the hashes are calculated correctly by checking for duplicates in the queue."""

        options = Options()
        queue = Queue(options)

        for x in range(0, 100):
            request = Request("https://example.ltd?1=1#2=2")
            HTTPRequestHelper.patch_with_options(request, options)
            request.cookies.set(name='tasty_cookie{}'.format(x), value='yum', domain='example.ltd')
            queue.add_request(request)

        self.assertEqual(queue.count_total, 1)

    def test_hash_option_protocol_must_match(self):
        """Ensure different protocols are treated separately if protocols must match is True."""

        options = Options()
        options.scope.protocol_must_match = True
        queue = Queue(options)

        queue.add_request(Request("https://example.ltd"))
        queue.add_request(Request("http://example.ltd"))
        queue.add_request(Request("ftp://example.ltd"))

        self.assertEqual(queue.count_total, 3)

    def test_hash_option_protocol_must_not_match(self):
        """Ensure different protocols are treated as one queue item if protocols must match is False."""

        options = Options()
        options.scope.protocol_must_match = False
        queue = Queue(options)

        queue.add_request(Request("https://example.ltd"))
        queue.add_request(Request("http://example.ltd"))
        queue.add_request(Request("ftp://example.ltd"))

        self.assertEqual(queue.count_total, 1)

    def test_hash_option_subdomain_must_match(self):
        """Ensure different subdomains are treated separately if subdomains must match is True."""

        options = Options()
        options.scope.subdomain_must_match = True
        queue = Queue(options)

        queue.add_request(Request("https://www.example.ltd"))
        queue.add_request(Request("https://webmail.example.ltd"))
        queue.add_request(Request("https://subdomain.example.ltd"))

        self.assertEqual(queue.count_total, 3)

    def test_hash_option_subdomain_must_not_match(self):
        """Ensure different subdomains are treated as one queue item if subdomains must match is False."""

        options = Options()
        options.scope.subdomain_must_match = False
        queue = Queue(options)

        queue.add_request(Request("https://www.example.ltd"))
        queue.add_request(Request("https://webmail.example.ltd"))
        queue.add_request(Request("https://subdomain.example.ltd"))

        self.assertEqual(queue.count_total, 1)

    def test_hash_different_query_order(self):
        """Ensure query parameters in different orders are treated as one queue item."""

        queue = Queue(Options())

        queue.add_request(Request("https://www.example.ltd?b=b&c=c&a=a"))
        queue.add_request(Request("https://www.example.ltd?b=b&a=a&c=c"))
        queue.add_request(Request("https://www.example.ltd?a=a&b=b&c=c"))

        self.assertEqual(queue.count_total, 1)