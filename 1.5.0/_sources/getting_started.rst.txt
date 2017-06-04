Getting started
===============

.. contents:: Table of Contents
   :depth: 2
   :local:

Minimal implementation
----------------------

.. code:: python

    # example.py

    from nyawc.Options import Options
    from nyawc.Crawler import Crawler
    from nyawc.CrawlerActions import CrawlerActions
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

    options = Options()

    options.callbacks.crawler_before_start = cb_crawler_before_start # Called before the crawler starts crawling. Default is a null route.
    options.callbacks.crawler_after_finish = cb_crawler_after_finish # Called after the crawler finished crawling. Default is a null route.
    options.callbacks.request_before_start = cb_request_before_start # Called before the crawler starts a new request. Default is a null route.
    options.callbacks.request_after_finish = cb_request_after_finish # Called after the crawler finishes a request. Default is a null route.

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))

Running the crawler
-------------------

In the foreground
~~~~~~~~~~~~~~~~~

``$ python example.py``

In the background
~~~~~~~~~~~~~~~~~

``$ python -u example.py > output.log``