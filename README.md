<p align="center">
    <img src="https://raw.githubusercontent.com/tijme/not-your-average-web-crawler/develop/.github/logo.png" width="300" height="300" alt="NYAWC">
    <br/>
    <a href="https://travis-ci.org/tijme/not-your-average-web-crawler"><img src="https://travis-ci.org/tijme/not-your-average-web-crawler.svg?branch=master" alt="Build Status"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/pypi/pyversions/nyawc.svg" alt="Python version"></a>
    <a href="https://pypi.python.org/pypi/nyawc/"><img src="https://img.shields.io/pypi/v/nyawc.svg" alt="PyPi version"></a>
    <a href="LICENSE.md"><img src="https://img.shields.io/pypi/l/nyawc.svg" alt="License: MIT"></a>
</p>

## Not Your Average Web Crawler
A very useful web crawler for vulnerability scanning. Not Your Average Web Crawler (N.Y.A.W.C) is a Python application that enables you to crawl web applications for requests instead of URLs. It crawls every GET and POST request on the specified domain and keeps track of the request and response data. It's main purpose is to be used in web application vulnerability scanners.

**Crawls:**

- **Links:** URLs in HTML, XML, etc.
- **Forms:** GET & POST forms and their request data.

**Future development:**
- Documentation/wiki improvements.
- Support rate limiting.
- Support XHR/JS scraping.
- Add other scrapers.

## Table of contents

  * [Installation](#installation)
  * [Crawling flow](#crawling-flow)
  * [Documentation](#documentation)
  * [Example usage](#example-usage)
  * [Testing](#testing)
  * [Issues](#issues)
  * [License](#license)

## Installation
First make sure you're on [Python 3.3](https://www.python.org/) or higher. Then run the command below to install N.Y.A.W.C.

`$ pip install --upgrade nyawc`

## Crawling flow

1. Add the start request to the queue.
2. Start first first request in the queue _(repeat until  `max threads` option reached)_.
3. Add all requests found in the response to the queue _(except duplicates)_.
4. Go to step #2 again to spawn new requests.

<img src="https://raw.githubusercontent.com/tijme/not-your-average-web-crawler/feature-hash-queue/.github/flow.png">

**Please note that if the queue is empty and all crawler threads are finished, the crawler will stop.**

## Documentation

Please refer to the [wiki](https://github.com/tijme/not-your-average-web-crawler/wiki) for all the documentation on N.Y.A.W.C.

## Example usage

You can use the callbacks in `example.py` to run your own exploit against the requests. If you want an example of automated exploit scanning, please take a look at [Angular CSTI scanner](https://github.com/tijme/angularjs-csti-scanner) (it uses N.Y.A.W.C to scan for the AngularJS sandbox escape vulnerability).

* `$ python example.py`
* `$ python -u example.py > output.log`

```python
# example.py

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
from nyawc.QueueItem import QueueItem
from nyawc.Crawler import Crawler, CrawlerActions
from nyawc.http.Request import Request

def cb_crawler_before_start():
    print("Crawler started.")

def cb_crawler_after_finish(queue):
    print("Crawler finished. Found " + str(queue.count_finished) + " requests.")

    for queue_item in queue.get_all(QueueItem.STATUS_FINISHED).values():
        print("[" + queue_item.request.method + "] " + queue_item.request.url + " (PostData: " + str(queue_item.request.data) + ")")

def cb_request_before_start(queue, queue_item):
    # return CrawlerActions.DO_SKIP_TO_NEXT
    # return CrawlerActions.DO_STOP_CRAWLING

    return CrawlerActions.DO_CONTINUE_CRAWLING

def cb_request_after_finish(queue, queue_item, new_queue_items):
    percentage = str(int(queue.get_progress()))
    total_requests = str(queue.count_total)

    print("At " + percentage + "% of " + total_requests + " requests ([" + str(queue_item.response.status_code) + "] " + queue_item.request.url + ").")

    # return CrawlerActions.DO_STOP_CRAWLING
    return CrawlerActions.DO_CONTINUE_CRAWLING

def cb_form_before_autofill(queue_item, elements, form_data):

    # return CrawlerActions.DO_NOT_AUTOFILL_FORM
    return CrawlerActions.DO_AUTOFILL_FORM

def cb_form_after_autofill(queue_item, elements, form_data):
    pass

# Declare the options
options = Options()

# Callback options
options.callbacks.crawler_before_start = cb_crawler_before_start
options.callbacks.crawler_after_finish = cb_crawler_after_finish
options.callbacks.request_before_start = cb_request_before_start
options.callbacks.request_after_finish = cb_request_after_finish
options.callbacks.form_before_autofill = cb_form_before_autofill
options.callbacks.form_after_autofill = cb_form_after_autofill

# Scope options
options.scope.protocol_must_match = False
options.scope.subdomain_must_match = False
options.scope.domain_must_match = True
options.scope.max_depth = None

# Identity options
options.identity.cookies.set(name='tasty_cookie', value='yum', domain='finnwea.com', path='/cookies')
options.identity.cookies.set(name='gross_cookie', value='blech', domain='finnwea.com', path='/elsewhere')
options.identity.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" # The user agent to make requests with. Default is Chrome.    
}

# Performance options
options.performance.max_threads = 8

crawler = Crawler(options)
crawler.start_with(Request("https://finnwea.com/"))
```

## Testing

The testing can and will automatically be done by [Travis CI](https://travis-ci.com/) on every push to the master branch. If you want to manually run the unit tests, use the command below.

`python -m unittest discover`

## Issues

Issues or new features can be reported via the GitHub issue tracker. Please make sure your issue or feature has not yet been reported by anyone else before submitting a new one.

## License

Not Your Average Web Crawler (N.Y.A.W.C) is open-sourced software licensed under the [MIT license](LICENSE.md).
