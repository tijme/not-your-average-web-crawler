<p align="center">
    <img src="https://i.imgur.com/ONCi3C2.png" width="300" height="300" alt="NYAWC">
    <br/>
    <a href="https://travis-ci.org/tijme/not-your-average-web-crawler">
        <img src="https://travis-ci.org/tijme/not-your-average-web-crawler.svg?branch=master" alt="Build Status">
    </a>
    <a href="LICENSE.md">
        <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
    </a>
</p>

## Not Your Average Web Crawler
A very useful web crawler for vulnerability scanning. Not Your Average Web Crawler (N.Y.A.W.C) is a Python application that enables you to crawl web applications for requests instead of URLs. It crawls every GET and POST request on the specified domain and keeps track of the request and response data. It's main purpose is to be used in web application vulnerability scanners like [Angular CSTI scanner](https://github.com/tijme/angular-csti-scanner).

**Crawls:**

- **Links:** URLs in HTML attributes, JSON, etc.
- **Forms:** GET & POST forms and their request data.

**Current limitations:**
- Only works on Python 3.6 or higher.
- Multiprocessing is not yet working.
- Maximum recursion depth exception when crawling too much resources.

**Future development:**

- Fix current limitations.
- Performance improvements.
- Support XHR crawling.
- Support XML & Open XML crawling.
- Support custom cookies.
- Support custom user agents.
- Support rate limiting.

## Installation
First make sure you're on [Python 3.6](https://www.python.org/) or higher. Then run the command below to install the dependencies.

`pip install nyawc`

## Example usage
```python
from nyawc.Options import Options
from nyawc.Crawler import Crawler, CrawlerActions
from nyawc.http.Request import Request

def cb_crawler_before_start():
    print("Crawler started.")

def cb_crawler_after_finish(queue):
    print("Crawler finished. Found " + str(queue.get_count()) + " requests.")

    for queue_item in queue.get_all():
        print(queue_item.request.method + ": " + queue_item.request.url + " (" + str(queue_item.request.data) + ")")

def cb_request_before_start(queue, queue_item):
    # return CrawlerActions.DO_SKIP_TO_NEXT
    # return CrawlerActions.DO_STOP_CRAWLING
    return CrawlerActions.DO_CONTINUE_CRAWLING

def cb_request_after_finish(queue, queue_item, new_queue_items):
    percentage = str(int(queue.get_progress()))
    total_requests = str(queue.get_count())

    print("At " + percentage + "% of " + total_requests + " requests (" + queue_item.request.url + ").")

    # return CrawlerActions.DO_STOP_CRAWLING
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
options.scope.subdomain_must_match = True # Only crawl pages with the same subdomain as the startpoint. If the startpoint is not a subdomain, no subdomains will be crawled. Default is True.
options.scope.domain_must_match = True # Only crawl pages with the same domain as the startpoint (e.g. only finnwea.com). Default is True.
options.scope.ignore_similar_requests = True # Ignore similar requests like `?page=1` & `?page=2` or `/page/1` and `/page/2`. Default is True.
options.scope.max_depth = None # The maximum search depth. For example, 2 would be the startpoint and all the pages found on it. Default is None (unlimited).

# Performance options
options.performance.max_processes = 8 # The maximum amount of simultaneous processes to use for crawling. Default is 8. 

crawler = Crawler(options)
crawler.start_with(Request("https://finnwea.com/"))
```

## Testing

The testing can and will automatically be done by [Travis CI](https://travis-ci.com/) on every push to the master branch. If you want to manually run the unit tests, use the command below.

`python -m unittest discover -s tests`

## Issues

Issues or new features can be reported via the GitHub issue tracker. Please make sure your issue or feature has not yet been reported by anyone else before submitting a new one.

## License

Not Your Average Web Crawler (N.Y.A.W.C) is open-sourced software licensed under the [MIT license](LICENSE.md).
