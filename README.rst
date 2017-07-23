.. raw:: html

    <p align="center">

.. image:: https://tijme.github.io/not-your-average-web-crawler/latest/_static/img/logo.svg?pypi=png.from.svg
    :width: 300px
    :height: 300px
    :alt: N.Y.A.W.C. logo
    :align: center

.. raw:: html

    <br class="title">

.. image:: https://travis-ci.org/tijme/not-your-average-web-crawler.svg?branch=master
    :target: https://travis-ci.org/tijme/not-your-average-web-crawler
    :alt: Build Status

.. image:: https://img.shields.io/pypi/pyversions/nyawc.svg
    :target: https://www.python.org/
    :alt: Python version

.. image:: https://img.shields.io/pypi/v/nyawc.svg
    :target: https://pypi.python.org/pypi/nyawc/
    :alt: PyPi version

.. image:: https://img.shields.io/pypi/l/nyawc.svg
    :target: https://github.com/tijme/not-your-average-web-crawler/blob/master/LICENSE.rst
    :alt: License: MIT

.. raw:: html

   </p>
   <h1>Not Your Average Web Crawler</h1>

Did you ever want to test your payload against all requests of a certain domain? N.Y.A.W.C can help you with that. It crawls all requests (e.g. GET, POST or PUT) on the specified domain and keeps track of the request and response data. During the crawling process, the callbacks enable you to insert your payload at specific places and test if they worked.

Table of contents
-----------------

-  `Installation <#installation>`__
-  `Crawling flow <#crawling-flow>`__
-  `Documentation <#documentation>`__
-  `Minimal implementation <#minimal-implementation>`__
-  `Testing <#testing>`__
-  `Issues <#issues>`__
-  `License <#license>`__

Installation
------------

First make sure you're on `Python 2.7/3.3 <https://www.python.org/>`__ or higher. Then run the command below to install N.Y.A.W.C.

``$ pip install --upgrade nyawc``

Crawling flow
-------------

1. You can define your startpoint (a request) and the crawling scope and then start the crawler.
2. The crawler repeatedly starts the first request in the queue until ``max threads`` is reached.
3. The crawler adds all requests found in the response to the end of the queue (except duplicates).
4. The crawler goes back to step #2 to spawn new requests repeatedly until ``max threads`` is reached.

.. image:: https://tijme.github.io/not-your-average-web-crawler/latest/_static/img/flow.svg
   :alt: N.Y.A.W.C crawling flow

**Please note that if the queue is empty and all crawler threads are finished, the crawler will stop.**

Documentation
-------------

Please refer to the `documentation <https://tijme.github.io/not-your-average-web-crawler/>`__ or the `API <https://tijme.github.io/not-your-average-web-crawler/latest/py-modindex.html>`__ for all the information about N.Y.A.W.C.

Minimal implementation
----------------------

You can use the callbacks in ``example_minimal.py`` to run your own exploit against the requests. If you want an example of automated exploit scanning, please take a look at `Detective <https://github.com/tijme/detective>`__ (it uses N.Y.A.W.C to scan for information disclosure vulnerabilities).

You can also use the `kitchen sink <https://tijme.github.io/not-your-average-web-crawler/latest/kitchen_sink.html>`__ (which contains all the functionalities from N.Y.A.W.C.) instead of the example below. The code below is a minimal implementation of N.Y.A.W.C.

-  ``$ python example_minimal.py``
-  ``$ python -u example_minimal.py > output.log``

.. code:: python

    # example_minimal.py

    from nyawc.Options import Options
    from nyawc.Crawler import Crawler
    from nyawc.CrawlerActions import CrawlerActions
    from nyawc.http.Request import Request

    def cb_crawler_before_start():
        print("Crawler started.")

    def cb_crawler_after_finish(queue):
        print("Crawler finished.")
        print("Found " + str(len(queue.get_all(QueueItem.STATUS_FINISHED))) + " requests.")

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

Testing
-------

The testing can and will automatically be done by `Travis CI <https://travis-ci.org/tijme/not-your-average-web-crawler>`__ on every push to the master branch. If you want to manually run the unit tests, use the command below.

``$ python -m unittest discover``

Issues
------

Issues or new features can be reported via the GitHub issue tracker. Please make sure your issue or feature has not yet been reported by anyone else before submitting a new one.

License
-------

Not Your Average Web Crawler (N.Y.A.W.C) is open-sourced software licensed under the `MIT license <https://github.com/tijme/not-your-average-web-crawler/blob/master/LICENSE.rst>`__.
