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

from nyawc.Options import Options
from nyawc.Crawler import Crawler
from nyawc.QueueItem import QueueItem
from nyawc.http.Request import Request

import unittest
import os
 
class TestSite(unittest.TestCase):
    """The TestSite class checks if the crawler handles invalid responses correctly."""

    def __init__(self, *args, **kwargs):
        super(TestSite, self).__init__(*args, **kwargs)
        self.travis = "UNITTEST_NYAWC_SITE" in os.environ or True

    def test_make_absolute(self):
        if not self.travis:
            print("\n\nPlease not that the 'TestSite' unit test did not run.")
            print("It will only run in Travis since it needs a webserver.")
            return

        options = Options()
        options.callbacks.crawler_after_finish
        crawler = Crawler(options)
        crawler.start_with(Request("http://localhost/"))

        self.assertEqual(crawler.queue.count_total, 16)
