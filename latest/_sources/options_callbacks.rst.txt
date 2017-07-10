Callbacks
=========

.. contents:: Table of Contents
   :depth: 2
   :local:

How to use callbacks
--------------------

.. code:: python

    # callbacks_example.py

    from nyawc.Options import Options
    from nyawc.Crawler import Crawler
    from nyawc.CrawlerActions import CrawlerActions
    from nyawc.http.Request import Request

    def cb_crawler_before_start():
        print("Started crawling")

    def cb_crawler_after_finish(queue):
        print("Finished crawling")

    def cb_request_before_start(queue, queue_item):
        print("Making request: {}".format(queue_item.request.url))
        return CrawlerActions.DO_CONTINUE_CRAWLING

    def cb_request_after_finish(queue, queue_item, new_queue_items):
        print("Finished request: {}".format(queue_item.request.url))
        return CrawlerActions.DO_CONTINUE_CRAWLING

    def cb_request_on_error(queue_item, message):
        print("A request failed with an error message.")
        print(message)

    def cb_form_before_autofill(queue_item, elements, form_data):
        return CrawlerActions.DO_AUTOFILL_FORM

    def cb_form_after_autofill(queue_item, elements, form_data):
        pass

    options = Options()

    options.callbacks.crawler_before_start = cb_crawler_before_start
    options.callbacks.crawler_after_finish = cb_crawler_after_finish
    options.callbacks.request_before_start = cb_request_before_start
    options.callbacks.request_after_finish = cb_request_after_finish
    options.callbacks.request_on_error = cb_request_on_error
    options.callbacks.form_before_autofill = cb_form_before_autofill
    options.callbacks.form_after_autofill = cb_form_after_autofill

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))

Available callbacks
-------------------

Before crawler start
~~~~~~~~~~~~~~~~~~~~

Can be used to run some code before the crawler starts crawling. It does not receive any arguments.

.. code:: python

    ...

    def cb_crawler_before_start():
        print("Started crawling")

    options.callbacks.crawler_before_start = cb_crawler_before_start

    ...

After crawler finish
~~~~~~~~~~~~~~~~~~~~

Can be used to run some code after the crawler finished crawling. It receives one argument, :class:`nyawc.Queue`.

-  ``queue.get_all()[0].request`` contains a :class:`nyawc.http.Request`.
-  ``queue.get_all()[0].response`` contains a :class:`nyawc.http.Response`.

.. code:: python

    ...

    def cb_crawler_after_finish(queue):
        # Print the amount of request/response pairs that were found.
        print("Crawler finished, found " + str(queue.count_total) + " requests.")

        # Iterate over all request/response pairs that were found.
        for queue_item in queue.get_all():
            print("Request method {}".format(queue_item.request.method))
            print("Request URL {}".format(queue_item.request.url))
            print("Request POST data {}".format(queue_item.request.data))
            # print("Response body {}".format(queue_item.response.text))

    options.callbacks.crawler_after_finish = cb_crawler_after_finish

    ...

Before request start
~~~~~~~~~~~~~~~~~~~~

Can be used to run some code after the request started executing. It receives two arguments, :class:`nyawc.Queue`, which contains all the items currently in the queue (also finished items) and :class:`nyawc.QueueItem`, which is the item (request/response pair) in the queue that will now be executed.

-  By returning ``CrawlerActions.DO_SKIP_TO_NEXT``, this queue\_item (request/response pair) will be skipped.
-  By returning ``CrawlerActions.DO_STOP_CRAWLING``, the crawler will stop crawling entirely.
-  When returning ``CrawlerActions.DO_CONTINUE_CRAWLING``, the crawler will continue like normally.

.. code:: python

    ...

    def cb_request_before_start(queue, queue_item):
        # return CrawlerActions.DO_SKIP_TO_NEXT
        # return CrawlerActions.DO_STOP_CRAWLING

        return CrawlerActions.DO_CONTINUE_CRAWLING

    options.callbacks.request_before_start = cb_request_before_start

    ...

After request finish
~~~~~~~~~~~~~~~~~~~~

Can be used to run some code after the request finished executing. It receives three arguments, :class:`nyawc.Queue`, which contains all the items currently in the queue (also finished items), :class:`nyawc.QueueItem`, which is the item (request/response pair) in the queue that will now be executed and ``new_queue_items`` (array of :class:`nyawc.QueueItem`), which contains the request/response pairs that were found during this request.

-  By returning ``CrawlerActions.DO_STOP_CRAWLING``, the crawler will stop crawling entirely.
-  When returning ``CrawlerActions.DO_CONTINUE_CRAWLING``, the crawler will continue like normally.

.. code:: python

    ...

    def cb_request_after_finish(queue, queue_item, new_queue_items):
        percentage = str(int(queue.get_progress()))
        total_requests = str(queue.count_total))

        print("At " + percentage + "% of " + total_requests + " requests ([" + str(queue_item.response.status_code) + "] " + queue_item.request.url + ").")

        # return CrawlerActions.DO_STOP_CRAWLING
        return CrawlerActions.DO_CONTINUE_CRAWLING

    options.callbacks.request_after_finish = cb_request_after_finish

    ...

On request error
~~~~~~~~~~~~~~~~

Can be used to run some code if a request failed to execute. It receives two arguments, :class:`nyawc.QueueItem`, which is the item (request/response pair) in the queue that will now be executed and ``message`` (str), which contains a detailed error message.

.. code:: python

    ...

    def cb_request_on_error(queue_item, message):
        print("A request failed with an error message.")
        print(message)

    options.callbacks.request_on_error = cb_request_on_error

    ...

Before form autofill
~~~~~~~~~~~~~~~~~~~~

Can be used to run some code before automatically filling in a form. It receives three arguments, :class:`nyawc.Queue`, which contains all the items currently in the queue (also finished items), ``elements``, which is an array of BeautifulSoup4 input elements found in the form and ``form_data``, which is the (editable) form data that will be used in the request.

-  By returning ``CrawlerActions.DO_AUTOFILL_FORM``, the form will be filled with random data.
-  By returning ``CrawlerActions.DO_NOT_AUTOFILL_FORM``, only default input values will be used.

.. code:: python

    ...

    def cb_form_before_autofill(queue_item, elements, form_data):
        # return CrawlerActions.DO_NOT_AUTOFILL_FORM

        return CrawlerActions.DO_AUTOFILL_FORM

    options.callbacks.form_before_autofill = cb_form_before_autofill

    ...

After form autofill
~~~~~~~~~~~~~~~~~~~

Can be used to run some code after the crawler automatically filled in a form. It receives three arguments, :class:`nyawc.Queue`, which contains all the items currently in the queue (also finished items), ``elements``, which is an array of BeautifulSoup4 input elements found in the form and ``form_data``, which is the (editable) form data that will be used in the request.

Please note that this callback will not be called if ``CrawlerActions.DO_NOT_AUTOFILL_FORM`` was returned in the before callback.

.. code:: python

    ...

    def cb_form_after_autofill(queue_item, elements, form_data):
        pass

    options.callbacks.form_after_autofill = cb_form_after_autofill

    ...
