<p align="center">
    <img src="https://raw.githubusercontent.com/tijme/not-your-average-web-crawler/master/.github/logo.png" width="300" height="300" alt="NYAWC">
    <br/>
    <a href="https://travis-ci.org/tijme/not-your-average-web-crawler"><img src="https://travis-ci.org/tijme/not-your-average-web-crawler.svg?branch=master" alt="Build Status"></a>
    <a href="https://www.python.org/"><img src="https://img.shields.io/pypi/pyversions/nyawc.svg" alt="Python version"></a>
    <a href="https://pypi.python.org/pypi/nyawc/"><img src="https://img.shields.io/pypi/v/nyawc.svg" alt="PyPi version"></a>
    <a href="LICENSE.md"><img src="https://img.shields.io/pypi/l/nyawc.svg" alt="License: MIT"></a>
</p>

## Not Your Average Web Crawler
A very useful web crawler for vulnerability scanning. Not Your Average Web Crawler (N.Y.A.W.C) is a Python application that enables you to crawl web applications for requests instead of URLs. It crawls every GET and POST request on the specified domain and keeps track of the request and response data. It's main purpose is to be used in web application vulnerability scanners.

**Crawls:**

- **Links:** URLs in HTML, JSON, XML, CSS, JSON, JavaScript, etc.
- **Forms:** GET & POST forms and their request data.

**Future development:**
- Wiki improvements.
- Performance improvements.
- Support rate limiting.
- Support XHR crawling.

## Installation
First make sure you're on [Python 3.3](https://www.python.org/) or higher. Then run the command below to install N.Y.A.W.C.

`pip install --upgrade nyawc`

## Documentation

Please refer to the [wiki](https://github.com/tijme/not-your-average-web-crawler/wiki) for all the documentation on N.Y.A.W.C.

## Example usage

You can use the callbacks in `example.py` to run your own exploit against the requests. If you want an example of automated exploit scanning, please take a look at [Angular CSTI scanner](https://github.com/tijme/angularjs-csti-scanner) (it uses N.Y.A.W.C to scan for the AngularJS sandbox escape vulnerability).

* `python example.py`
* `python -u example.py > output.log`

```python
# example.py

from nyawc.Options import Options
from nyawc.Crawler import Crawler, CrawlerActions
from nyawc.http.Request import Request

def cb_crawler_before_start():
    print("Crawler started.")

def cb_crawler_after_finish(queue):
    print("Crawler finished, found " + str(queue.get_count()) + " requests.")

def cb_request_before_start(queue, queue_item):
    print("Starting: {}".format(queue_item.request.url))
    return CrawlerActions.DO_CONTINUE_CRAWLING

def cb_request_after_finish(queue, queue_item, new_queue_items):
    print("Finished: {}".format(queue_item.request.url))
    return CrawlerActions.DO_CONTINUE_CRAWLING

# Declare the options
options = Options()

# Callback options
options.callbacks.crawler_before_start = cb_crawler_before_start # Called before the crawler starts crawling. Default is a null route.
options.callbacks.crawler_after_finish = cb_crawler_after_finish # Called after the crawler finished crawling. Default is a null route.
options.callbacks.request_before_start = cb_request_before_start # Called before the crawler starts a new request. Default is a null route.
options.callbacks.request_after_finish = cb_request_after_finish # Called after the crawler finishes a request. Default is a null route.

# Scope options
options.scope.protocol_must_match = False # Only crawl pages with the same protocol as the startpoint (e.g. only https). Default is False.
options.scope.subdomain_must_match = False # Only crawl pages with the same subdomain as the startpoint. If the startpoint is not a subdomain, no subdomains will be crawled. Default is True.
options.scope.domain_must_match = True # Only crawl pages with the same domain as the startpoint (e.g. only finnwea.com). Default is True.
options.scope.ignore_similar_requests = True # Ignore similar requests like `?page=1` & `?page=2` or `/page/1` and `/page/2`. Default is False.
options.scope.max_depth = None # The maximum search depth. For example, 2 would be the startpoint and all the pages found on it. Default is None (unlimited).

# Identity options
options.identity.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" # The user agent to make requests with. Default is Chrome.

# Performance options
options.performance.max_threads = 8 # The maximum amount of simultaneous threads to use for crawling. Default is 4.

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
