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

class CookieHelper:
    """A helper for cookie jars."""

    @staticmethod
    def are_cookies_the_same(jar1, jar2):
        """Check if the given cookies are the same.

        Args:
            jar1 (str): The first cookie jar.
            jar1 (str): The second cookie jar.

        Returns:
            bool: If the cookies are the same

        """


        if jar1 is None and jar2 is not None:
            return False

        if jar2 is None and jar1 is not None:
            return False

        if jar1 is None and jar2 is None:
            return True

        cookieMatches = False
        for cookie1 in jar1:
            for cookie2 in jar2:
                if cookie1.name == cookie2.name:
                    if cookie1.value == cookie2.value:
                        cookieMatches = True

        if not cookieMatches:
            return False

        cookieMatches = False
        for cookie2 in jar2:
            for cookie1 in jar1:
                if cookie2.name == cookie1.name:
                    if cookie2.value == cookie1.value:
                        cookieMatches = True

        if not cookieMatches:
            return False
                
        return True

    @staticmethod
    def are_cookies_similar(jar1, jar2):
        """Check if the given cookies are similar.

        Args:
            jar1 (str): The first cookie jar.
            jar1 (str): The second cookie jar.

        Returns:
            bool: If the cookies are similar

        """

        return True

        if jar1 is None and jar2 is not None:
            return False

        if jar2 is None and jar1 is not None:
            return False

        if jar1 is None and jar2 is None:
            return True

        for cookie1 in jar1:
            cookieMatches = False
            for cookie2 in jar2:
                if cookie1.name == cookie2.name:
                    cookieMatches = True

        if not cookieMatches:
            return False

        for cookie2 in jar2:
            cookieMatches = False
            for cookie1 in jar1:
                if cookie2.name == cookie1.name:
                    cookieMatches = True

        if not cookieMatches:
            return False
                
        return True