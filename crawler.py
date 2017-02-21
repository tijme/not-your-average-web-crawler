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

from src.Crawler import Crawler
from src.Request import Request

def crawler_started():
    print("crawler_started")

def crawler_request_started(queue, started_request):
    #print("Crawling: {}".format(started_request.req_url))
    return True
    
def crawler_request_finished(queue, finished_request, found_requests):
    message = "Crawled {}/{}.".format(queue.get_count_without(Request.STATUS_QUEUED), queue.get_count())

    if len(found_requests) > 0:
        message += " Found {} requests, these will be added to the queue (ignoring any duplicates).".format(len(found_requests))
    else:
        message += " No additional requests found."

    print(message)

    return True

def crawler_finished(requests):
    print("crawler_finished")
    print("")
    print("")

    for request in requests:
        print("Found: {}".format(request.req_url))

def main():
    crawler = Crawler(Request("https://finnwea.com/", Request.METHOD_GET))

    crawler.cb_crawler_started = crawler_started
    crawler.cb_crawler_request_started = crawler_request_started
    crawler.cb_crawler_request_finished = crawler_request_finished
    crawler.cb_crawler_finished = crawler_finished

    #crawler.opt_max_depth = 3
    #crawler.opt_max_processes = 8
    crawler.opt_domain_must_match = True

    crawler.start()

if __name__ == "__main__":
    main()