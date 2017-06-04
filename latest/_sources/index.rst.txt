Welcome to the N.Y.A.W.C documentation
======================================

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

A very useful web crawler for vulnerability scanning. Not Your Average Web Crawler (N.Y.A.W.C) is a Python application that enables you to crawl web applications for requests instead of URLs. It crawls every GET and POST request on the specified domain and keeps track of the request and response data. It's main purpose is to be used in web application vulnerability scanners

How it works
------------

1. Add your start request to the queue.
2. Crawler starts first request in the queue *(repeats until ``max threads`` option reached)*.
3. Crawler adds all requests found in the response to the queue *(except duplicates)*.
4. Crawler goes to step #2 again to spawn new requests.

.. image:: https://tijme.github.io/not-your-average-web-crawler/latest/_static/flow.svg
   :alt: N.Y.A.W.C crawling flow

**Please note that if the queue is empty and all crawler threads are finished, the crawler will stop.**
