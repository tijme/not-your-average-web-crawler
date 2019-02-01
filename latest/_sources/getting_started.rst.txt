.. title:: Getting Started

Minimal example
---------------

N.Y.A.W.C does not have a CLI entry point, so you need to create one yourself. Save the code below as ``example.py``. The example code prints all request URLs that were found by the crawler.

.. code:: python

    # example.py

    from nyawc.Options import Options
    from nyawc.Crawler import Crawler
    from nyawc.QueueItem import QueueItem
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

Testing example.py
------------------

In the foreground
~~~~~~~~~~~~~~~~~

Output all contents to the console.

``$ python example.py``

In the background
~~~~~~~~~~~~~~~~~

Output all contents to a file and run the process in the background.

``$ python -u example.py > output.log``

Adding extra options
--------------------

Callbacks
~~~~~~~~~

All the available callbacks are documented `here <options_callbacks.html>`_.

Scope
~~~~~

You can set scope options to, for example, only crawl certain subdomains or certain request methods. See `this <options_crawling_scope.html>`_ page for all the available scope options.

Identity
~~~~~~~~

Do you want to use authentication, set headers or use a proxy? Check `these <options_crawling_identity.html>`_ identity options for documentation.

Routing
~~~~~~~

If you want to ignore similar requests (e.g. /news/1, /news/2, /news/3, etc) you can specify routes via the `routing <options_routing.html>`_ options.

The kitchen sink
----------------

The kitchen sink is an example that implements all the features/options of N.Y.A.W.C. The kitchen sink is available for copy paste. `Check it out <kitchen_sink.html>`_!
