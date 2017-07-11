Kitchen sink
============

The English phrase "Everything but the kitchen sink" means "almost anything one can think of". The example below contains all the functionalities from N.Y.A.W.C.

.. code:: python

    # example.py

    from nyawc.Options import Options
    from nyawc.QueueItem import QueueItem
    from nyawc.Crawler import Crawler
    from nyawc.CrawlerActions import CrawlerActions
    from nyawc.http.Request import Request
    from requests.auth import HTTPBasicAuth

    def cb_crawler_before_start():
        print("Crawler started.")

    def cb_crawler_after_finish(queue):
        print("Crawler finished.")
        print("Found " + str(queue.count_finished) + " requests.")

        for queue_item in queue.get_all(QueueItem.STATUS_FINISHED).values():
            print("[" + queue_item.request.method + "] " + queue_item.request.url + " (PostData: " + str(queue_item.request.data) + ")")

    def cb_request_before_start(queue, queue_item):
        # return CrawlerActions.DO_SKIP_TO_NEXT
        # return CrawlerActions.DO_STOP_CRAWLING

        return CrawlerActions.DO_CONTINUE_CRAWLING

    def cb_request_after_finish(queue, queue_item, new_queue_items):
        percentage = str(int(queue.get_progress()))
        total_requests = str(queue.count_total)

        print("At " + percentage + "% of " + total_requests + " requests ([" + str(queue_item.response.status_code) + "] " + queue_item.request.url + ").")

        # return CrawlerActions.DO_STOP_CRAWLING
        return CrawlerActions.DO_CONTINUE_CRAWLING

    def cb_request_in_thread_before_start(queue_item):
        pass

    def cb_request_in_thread_after_finish(queue_item):
        pass

    def cb_request_on_error(queue_item, message):
        print("A request failed with an error message.")
        print(message)

    def cb_form_before_autofill(queue_item, elements, form_data):

        # return CrawlerActions.DO_NOT_AUTOFILL_FORM
        return CrawlerActions.DO_AUTOFILL_FORM

    def cb_form_after_autofill(queue_item, elements, form_data):
        pass

    # Declare the options
    options = Options()

    # Callback options
    options.callbacks.crawler_before_start = cb_crawler_before_start # Called before the crawler starts crawling. Default is a null route.
    options.callbacks.crawler_after_finish = cb_crawler_after_finish # Called after the crawler finished crawling. Default is a null route.
    options.callbacks.request_before_start = cb_request_before_start # Called before the crawler starts a new request. Default is a null route.
    options.callbacks.request_after_finish = cb_request_after_finish # Called after the crawler finishes a request. Default is a null route.
    options.callbacks.request_in_thread_before_start = cb_request_in_thread_before_start # Called in the crawling thread (when it started). Default is a null route.
    options.callbacks.request_in_thread_after_finish = cb_request_in_thread_after_finish # Called in the crawling thread (when it finished). Default is a null route.
    options.callbacks.request_on_error = cb_request_on_error # Called if a request failed. Default is a null route.
    options.callbacks.form_before_autofill = cb_form_before_autofill # Called before the crawler autofills a form. Default is a null route.
    options.callbacks.form_after_autofill = cb_form_after_autofill # Called after the crawler autofills a form. Default is a null route.

    # Scope options
    options.scope.protocol_must_match = False # Only crawl pages with the same protocol as the startpoint (e.g. only https). Default is False.
    options.scope.subdomain_must_match = True # Only crawl pages with the same subdomain as the startpoint. If the startpoint is not a subdomain, no subdomains will be crawled. Default is True.
    options.scope.hostname_must_match = True # Only crawl pages with the same hostname as the startpoint (e.g. only `finnwea`). Default is True.
    options.scope.tld_must_match = True # Only crawl pages with the same tld as the startpoint (e.g. only `.com`). Default is True.
    options.scope.max_depth = None # The maximum search depth. 0 only crawls the start request. 1 will also crawl all the requests found on the start request. 2 goes one level deeper, and so on. Default is None (unlimited).
    options.scope.request_methods = [
        # The request methods to crawl. Default is all request methods
        Request.METHOD_GET,
        Request.METHOD_POST,
        Request.METHOD_PUT,
        Request.METHOD_DELETE,
        Request.METHOD_OPTIONS,
        Request.METHOD_HEAD
    ]

    # Identity options
    options.identity.auth = HTTPBasicAuth('user', 'pass') # Or any other authentication (http://docs.python-requests.org/en/master/user/authentication/). Default is None.
    options.identity.cookies.set(name='tasty_cookie', value='yum', domain='finnwea.com', path='/cookies')
    options.identity.cookies.set(name='gross_cookie', value='blech', domain='finnwea.com', path='/elsewhere')
    options.identity.proxies = {
        # No authentication
        # 'http': 'http://host:port',
        # 'https': 'http://host:port',

        # Basic authentication
        # 'http': 'http://user:pass@host:port',
        # 'https': 'https://user:pass@host:port',

        # SOCKS
        # 'http': 'socks5://user:pass@host:port',
        # 'https': 'socks5://user:pass@host:port'
    }
    options.identity.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    })

    # Performance options
    options.performance.max_threads = 10 # The maximum amount of simultaneous threads to use for crawling. Default is 8.
    options.performance.request_timeout = 10 # The request timeout in seconds (throws an exception if exceeded). Default is 30.

    # Misc options
    options.misc.debug = False # If debug is enabled extra information will be logged to the console. Default is False.

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))
