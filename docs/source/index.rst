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

What is N.Y.A.W.C?
------------------

A very useful web crawler for vulnerability scanning. Not Your Average Web Crawler (N.Y.A.W.C) is a Python 3 application that enables you to crawl web applications for requests instead of URLs. It crawls every GET and POST request on the specified domain and keeps track of the request and response data. It's main purpose is to be used as a web application vulnerability scanner.

What is it for?
---------------

It helps you to execute your own exploit against all resources on a domain without having to worry about the latter. N.Y.A.W.C does all the crawling work for you. You can use the callbacks to implement your exploit and then sit back and relax.

What does it solve?
-------------------

It saves your precious time because you no longer have to worry about the crawling mechanism and the maintenance of it. N.Y.A.W.C ensures that you can focus on the exploiting itself.