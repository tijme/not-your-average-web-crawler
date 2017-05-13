Crawling identity
=================

.. contents:: Table of Contents
   :depth: 2
   :local:

How to use identity options
---------------------------

.. code:: python

    # identity_example.py

    from nyawc.Options import Options
    from nyawc.Crawler import Crawler
    from nyawc.http.Request import Request

    options = Options()

    options.identity.cookies.set(name='tasty_cookie', value='yum', domain='finnwea.com', path='/cookies')
    options.identity.cookies.set(name='gross_cookie', value='blech', domain='finnwea.com', path='/elsewhere')
    options.identity.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))

Available identity options
--------------------------

**Cookies**

Set custom cookies for the crawler. Please check `python-requests <http://docs.python-requests.org/en/master/user/quickstart/#cookies>`__ cookie jar for all the cookie options.

.. code:: python

    options.identity.cookies.set(name='tasty_cookie', value='yum', domain='finnwea.com', path='/cookies')

**Headers**

Set custom headers for the crawler (as {key: value} object). For example, you can set a new user agent by using ``User-Agent`` as key, as shown below.

.. code:: python

    options.identity.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" # The user agent to make requests with. Default is Chrome.    
    }