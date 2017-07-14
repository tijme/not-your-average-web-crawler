.. title:: Crawling scope

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
    options.scope.hostname_must_match = True
    options.scope.tld_must_match = True
    options.scope.max_depth = None
    options.scope.request_methods = [
        Request.METHOD_GET,
        Request.METHOD_POST,
        Request.METHOD_PUT,
        Request.METHOD_DELETE,
        Request.METHOD_OPTIONS,
        Request.METHOD_HEAD
    ]

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))

Available scope options
-----------------------

**Protocol must match**

Only crawl pages with the same protocol as the startpoint (e.g. only https) if True. Default is False.

.. code:: python

    options.scope.protocol_must_match = False

**Subdomain must match**

Only crawl pages with the same subdomain as the startpoint if True. If the startpoint is not a subdomain, no subdomains will be crawled. Default is True.

.. code:: python

    options.scope.subdomain_must_match = True

**Hostname must match**

Only crawl pages with the same hostname as the startpoint (e.g. only `finnwea`) if True. Default is True.

Please note that if you set this to false, chances are that it never stops crawling.

.. code:: python

    options.scope.hostname_must_match = True

**TLD must match**

Only crawl pages with the same tld as the startpoint (e.g. only `.com`) if True. Default is True.

.. code:: python

    options.scope.tld_must_match = True

**Maximum crawling depth**

The maximum search depth. Default is None (unlimited).

-  0 will only crawl the start request.
-  1 will also crawl all requests found on the start request.
-  2 will go one level deeper.
-  And so on...

.. code:: python

    options.scope.max_depth = None

**Allowed request methods**

Only crawl these request methods. If empty or ``None`` all request methods will be crawled. Default is all.

.. code:: python

    options.scope.request_methods = [
        Request.METHOD_GET,
        Request.METHOD_POST,
        Request.METHOD_PUT,
        Request.METHOD_DELETE,
        Request.METHOD_OPTIONS,
        Request.METHOD_HEAD
    ]
