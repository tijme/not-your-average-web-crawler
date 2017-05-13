Performance
===========

.. contents:: Table of Contents
   :depth: 2
   :local:

How to use performance options
------------------------------

.. code:: python

    # performance_example.py

    from nyawc.Options import Options
    from nyawc.Crawler import Crawler
    from nyawc.http.Request import Request

    options = Options()

    options.performance.max_threads = 10

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))

Available performance options
-----------------------------

**Maximum threads**

The maximum amount of simultaneous threads to use for crawling. Default is 8.

``options.performance.max_threads = 8``