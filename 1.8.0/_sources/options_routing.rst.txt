.. title:: Routing

How to use routing options
--------------------------

.. code:: python

    # misc_example.py

    from nyawc.Options import Options
    from nyawc.Crawler import Crawler
    from nyawc.http.Request import Request

    options = Options()

    options.routing.minimum_threshold = 4
    options.routing.routes = [ 
        "^(https?:\/\/)?(www\.)?finnwea\.com\/blog\/[^\n \/]+\/$"
    ]

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))

Available routing options
-------------------------

Minimum threshold
~~~~~~~~~~~~~~~~~

The minimum amount of requests to crawl (matching a certain route) before ignoring the rest. Default is 20.

For example, lets say we have these rquests;

.. code::

    https://finnwea.com/blog/1
    https://finnwea.com/blog/2
    https://finnwea.com/blog/3
    ...
    https://finnwea.com/blog/54

It will only crawl the first 20 requests. After that it ignores the rest of the blog posts.

**Please note that it will probably crawl a bit more than the minimum threshold depending on the maximum amount of threads to use.**

``options.routing.minimum_threshold = 20``

Routes
~~~~~~

The regular expressions that represent routes that should not be cralwed more times than the minimum treshold. Default is an empty array.

For example the route below represents ``http://finnwea.com/blog/{a-variable-blog-alias}/``.

``options.routing.routes = ["^(https?:\/\/)?(www\.)?finnwea\.com\/blog\/[^\n \/]+\/$"]``