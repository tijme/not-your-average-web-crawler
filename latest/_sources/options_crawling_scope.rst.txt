Crawling scope
==============

.. contents:: Table of Contents
   :depth: 2
   :local:

How to use scope options
------------------------

.. code:: python

    # scope_example.py

    from nyawc.Options import Options
    from nyawc.Crawler import Crawler
    from nyawc.http.Request import Request

    options = Options()

    options.scope.protocol_must_match = False
    options.scope.subdomain_must_match = True
    options.scope.domain_must_match = True
    options.scope.max_depth = None 

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))

Available scope options
-----------------------

**Protocol must match**

Only crawl pages with the same protocol as the startpoint (e.g. only https) if True. Default is False.

``options.scope.protocol_must_match = False``

**Subdomain must match**

Only crawl pages with the same subdomain as the startpoint if True. If the startpoint is not a subdomain, no subdomains will be crawled. Default is True.

``options.scope.subdomain_must_match = True``

**Domain must match**

Only crawl pages with the same domain as the startpoint (e.g. only finnwea.com) if True. Default is True.

Please note that if you set this to false, chances are that it never stops crawling.

``options.scope.domain_must_match = True``

**Maximum crawling depth**

The maximum search depth. Default is None (unlimited).

-  0 will only crawl the start request.
-  1 will also crawl all requests found on the start request.
-  2 will go one level deeper.
-  And so on...

``options.scope.max_depth = None``
