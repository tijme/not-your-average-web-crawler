.. title:: Misc

How to use misc options
------------------------------

.. code:: python

    # misc_example.py

    from nyawc.Options import Options
    from nyawc.Crawler import Crawler
    from nyawc.http.Request import Request

    options = Options()

    options.misc.debug = False

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))

Available misc options
----------------------

Debug
~~~~~

If debug is enabled extra information will be logged to the console. Default is False.

``options.misc.debug = True``
