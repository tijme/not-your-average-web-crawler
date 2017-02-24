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

from src.Options import Options
from src.Crawler import Crawler, CrawlerActions
from src.http.Request import Request

def cb_crawler_before_start():
    print("Crawler started.")

def cb_crawler_after_finish():
    print("Crawler finished.")

def cb_request_before_start():
    print("Crawler request started.")

    # return CrawlerActions.DO_SKIP_TO_NEXT
    # return CrawlerActions.DO_STOP_CRAWLING
    return CrawlerActions.DO_CONTINUE_CRAWLING

def cb_request_after_finish():
    print("Crawler request finished.")

    # return CrawlerActions.DO_STOP_CRAWLING
    return CrawlerActions.DO_CONTINUE_CRAWLING


# Declare the options
options = Options()

# Callback options
options.callbacks.crawler_before_start = cb_crawler_before_start # Called when the crawler starts crawling. Default is a null route.
options.callbacks.crawler_after_finish = cb_crawler_after_finish # Called when the crawler finished crawling. Default is a null route.
options.callbacks.request_before_start = cb_request_before_start # Called when the crawler starts a new request. Default is a null route.
options.callbacks.request_after_finish = cb_request_after_finish # Called when the crawler finishes a request. Default is a null route.

# Scope options
options.scope.protocol_must_match = False # Only crawl pages with the same protocol as the startpoint (e.g. only https). Default is False.
options.scope.subdomain_must_match = True # Only crawl pages with the same subdomain as the startpoint. If the startpoint is not a subdomain, no subdomains will be crawled. Default is True.
options.scope.domain_must_match = True # Only crawl pages with the same domain as the startpoint (e.g. only finnwea.com). Default is True.

# Performance options
options.performance.max_processes = 8 # The maximum amount of simultaneous processes to use for crawling. Default is 8. 
options.performance.max_depth = 10 # The maximum search depth. For example, 2 would be the startpoint and all the pages found on it. Default is None (unlimited).

crawler = Crawler(options)
crawler.start_with(Request("https://finnwea.com/"))