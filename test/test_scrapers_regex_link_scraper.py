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

from nyawc.scrapers.RegexLinkScraper import RegexLinkScraper
from nyawc.Queue import Queue, QueueItem
from nyawc.http.Request import Request
from nyawc.http.Response import Response

import unittest
 
class TestScrapersRegexLinkScraper(unittest.TestCase):
    """The TestScrapersRegexLinkScraper tests if the RegexLinkScraper is working correctly.

    Attributes:
        __host str: The host were the new URLs were found on
        __urls list(obj): The URLs that were found

    """

    __host = "https://example.ltd/"

    __urls = [
        {"url": """https://example.ltd?unique=1""", "must_pass": True, "test": """<a href="https://example.ltd?unique=1">test</a>"""},
        {"url": """https://example.ltd/?unique=2""", "must_pass": True, "test": """<a href="https://example.ltd/?unique=2">test</a>"""},
        {"url": """http://example.ltd?unique=3""", "must_pass": True, "test": """<a href="http://example.ltd?unique=3">test</a>"""},
        {"url": """http://example.ltd/?unique=4""", "must_pass": True, "test": """<a href="http://example.ltd/?unique=4">test</a>"""},
        {"url": """https://example.ltd?unique=5""", "must_pass": True, "test": """<a href="//example.ltd?unique=5">test</a>"""},
        {"url": """https://example.ltd/?unique=6""", "must_pass": True, "test": """<a href="//example.ltd/?unique=6">test</a>"""},
        {"url": """https://example.ltd/?unique=7""", "must_pass": True, "test": """<a a="b" c=d href="//example.ltd/?unique=7">test</a>"""},
        {"url": """https://example.ltd/?unique=8""", "must_pass": True, "test": """<a href="//example.ltd/?unique=8" a=b c="d">test</a>"""},
        {"url": """https://example.ltd/?unique=9""", "must_pass": True, "test": """<a a="b" c=d href="//example.ltd/?unique=9" a=b c="d">test</a>"""},
        {"url": """https://example.ltd/index.php?unique=10""", "must_pass": True, "test": """<a href="https://example.ltd/index.php?unique=10">test</a>"""},
        {"url": """https://example.ltd/index.php?unique=11&d=c""", "must_pass": True, "test": """<a href="https://example.ltd/index.php?unique=11&d=c">test</a>"""},
        {"url": """https://example.ltd/index.php?unique=12&utf8=✓""", "must_pass": True, "test": """<a href="https://example.ltd/index.php?unique=12&utf8=✓">test</a>"""},
        {"url": """https://example.ltd/index.php?unique=13#anchor""", "must_pass": True, "test": """<a href="https://example.ltd/index.php?unique=13#anchor">test</a>"""},
        {"url": """https://example.ltd/folder1/folder2/folder3?unique=14""", "must_pass": True, "test": """<a href="https://example.ltd/folder1/folder2/folder3?unique=14">test</a>"""},
        {"url": """https://example.ltd/folder1/../folder2/folder3?unique=15""", "must_pass": True, "test": """<a href="https://example.ltd/folder1/../folder2/folder3?unique=15">test</a>"""},
        {"url": """https://example.ltd/../folder1/folder2/folder3?unique=16""", "must_pass": True, "test": """<a href="https://example.ltd/../folder1/folder2/folder3?unique=16">test</a>"""},
        {"url": """https://example.ltd/folder1/folder2/folder3?unique=17""", "must_pass": True, "test": """<a href="/folder1/folder2/folder3?unique=17">test</a>"""},
        {"url": """https://example.ltd/folder1/folder2/folder3?unique=18""", "must_pass": True, "test": """<a href="../folder1/folder2/folder3?unique=18">test</a>"""},
        {"url": """https://example.ltd/folder1/folder2/folder3?unique=19""", "must_pass": True, "test": """<a href="../../folder1/folder2/folder3?unique=19">test</a>"""},
        {"url": """https://example.ltd/folder1/folder2/folder3?unique=20""", "must_pass": True, "test": """<a href="/../../folder1/folder2/folder3?unique=20">test</a>"""},
        {"url": """https://example.ltd/?unique=21""", "must_pass": True, "test": """<a href='https://example.ltd/?unique=21'>test</a>"""},
        {"url": """https://example.ltd/?unique=22""", "must_pass": True, "test": """<a href=`https://example.ltd/?unique=22`>test</a>"""},
        {"url": """https://example.ltd/unique=23/folder'/?unique=23""", "must_pass": True, "test": """<a href=`https://example.ltd/unique=23/folder'/?unique=23`>test</a>"""},
        {"url": """https://example.ltd/unique=24/folder"/?unique=24""", "must_pass": True, "test": """<a href=`https://example.ltd/unique=24/folder"/?unique=24`>test</a>"""},
        {"url": """https://example.ltd/unique=25/folder'/?unique=25""", "must_pass": True, "test": """<a href="https://example.ltd/unique=25/folder'/?unique=25">test</a>"""},
        {"url": """https://example.ltd/unique=26/folder`/?unique=26""", "must_pass": True, "test": """<a href="https://example.ltd/unique=26/folder`/?unique=26">test</a>"""},
        {"url": """https://example.ltd/unique=27/folder"/?unique=27""", "must_pass": True, "test": """<a href='https://example.ltd/unique=27/folder"/?unique=27'>test</a>"""},
        {"url": """https://example.ltd/unique=28/folder`/?unique=28""", "must_pass": True, "test": """<a href='https://example.ltd/unique=28/folder`/?unique=28'>test</a>"""},
        {"url": """https://example.ltd/unique=29/folder`/?unique=29""", "must_pass": True, "test": """<a href='https://example.ltd/unique=29/folder`/?unique=29'&b=not-included'>test</a>"""},
        {"url": """https://example.ltd/unique=30/folder`/?unique=30'&b=included""", "must_pass": True, "test": """<a href="https://example.ltd/unique=30/folder`/?unique=30'&b=included">test</a>"""},

        {"url": None, "must_pass": False, "test": """<a href="https:/example.ltd?unique=-1">"""},
        {"url": None, "must_pass": False, "test": """<a href="https:example.ltd/?unique=-2">"""},
        {"url": None, "must_pass": False, "test": """<a href="http/example.ltd/?unique=-3">"""},
        {"url": None, "must_pass": False, "test": """http:/example.ltd/?unique=-4"""},
        {"url": None, "must_pass": False, "test": """https:/example.ltd/?unique=-5"""},
        {"url": None, "must_pass": False, "test": """https:example.ltd/?unique=-6"""},
        {"url": None, "must_pass": False, "test": """https/example.ltd/?unique=-7"""},
        {"url": None, "must_pass": False, "test": """/folder1/folder2/folder3/folder4?unique=-8"""},
        {"url": None, "must_pass": False, "test": """/folder1/folder2/folder3/folder4/?unique=-9"""},
        {"url": None, "must_pass": False, "test": """/folder1/folder2/folder3/folder4/?unique=-10&a=b"""},
        {"url": None, "must_pass": False, "test": """/folder1/folder2/folder3/folder4/?unique=-11#anchor"""},
        {"url": None, "must_pass": False, "test": """<a href="http://examp\nle.ltd/?unique=-13">"""},
        {"url": None, "must_pass": False, "test": """var json = {"url": "https://example.ltd/?unique=-14"}"""},
        {"url": None, "must_pass": False, "test": """var json = {"url": 'https://example.ltd/?unique=-14'}"""}
    ]

    def test_regex_url_count(self):
        """Test if the amount of URLs found complies with the expected amount."""

        html = ""
        for url in self.__urls:
            html += "\n" + url["test"]

        finder = RegexLinkScraper(QueueItem(Request(""), Response()))
        matches = finder.get_requests_from_content(self.__host, html)

        self.assertEqual(len(matches), 30)
 
    def test_regex_url_matches(self):
        """Test if all the URLs match the found URLs."""
        
        for url in self.__urls:
            finder = RegexLinkScraper(QueueItem(Request(""), Response()))
            requests = finder.get_requests_from_content(self.__host, url["test"])

            if url["must_pass"]:
                self.assertEqual(len(requests), 1)
                self.assertEqual(requests[0].url, url["url"])
            else:
                self.assertEqual(len(requests), 0)
