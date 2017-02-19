import unittest

from src.finders.SoupLinkFinder import SoupLinkFinder
 
class TestFindersRegexLinkFinder(unittest.TestCase):

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
        {"url": """https://example.ltd/sample/page/1?unique=31""", "must_pass": True, "test": """<a href="sample/page/1?unique=31">test</a>"""},
        {"url": """https://example.ltd/page/2?unique=32""", "must_pass": True, "test": """<a href="/page/2?unique=32">test</a>"""},
        {"url": """https://example.ltd/page/3?unique=33""", "must_pass": True, "test": """<a href="page/3?unique=33">test</a>"""},
        {"url": """https://example.ltd/page4?unique=34""", "must_pass": True, "test": """<a href="page4?unique=34">test</a>"""}
    ]

    def test_soup_url_count(self):
        html = ""
        for url in self.__urls:
            html += "\n" + url["test"]

        finder = SoupLinkFinder(self.__host, html)
        matches = finder.get_requests()

        self.assertEqual(len(matches), 34)
 
    def test_soup_url_matches(self):
        for url in self.__urls:
            finder = SoupLinkFinder(self.__host, url["test"])
            matches = finder.get_requests()

            if url["must_pass"]:
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0].req_url, url["url"])
            else:
                self.assertEqual(len(matches), 0)
