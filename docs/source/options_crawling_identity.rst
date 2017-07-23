.. title:: Crawling identity

How to use identity options
---------------------------

.. code:: python

    # identity_example.py

    from nyawc.Options import Options
    from nyawc.Crawler import Crawler
    from nyawc.http.Request import Request

    options = Options()

    options.identity.auth = HTTPBasicAuth('user', 'pass')
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
        'http': 'socks5://user:pass@host:port',
        'https': 'socks5://user:pass@host:port'
    }
    options.identity.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    })

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))

Available identity options
--------------------------

Authentication
~~~~~~~~~~~~~~

Set the authentication for the crawler. Please check `python-requests <http://docs.python-requests.org/en/master/user/authentication/>`__ authentication for all the options. Default is None (no authentication).

You can find examples of different types of authentication below.

.. code:: python

    from requests.auth import HTTPBasicAuth
    options.identity.auth = HTTPBasicAuth('user', 'pass')

    from requests.auth import HTTPDigestAuth
    options.identity.auth = HTTPDigestAuth('user', 'pass')

    from requests_oauthlib import OAuth1
    options.identity.auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')

Cookies
~~~~~~~

Set custom cookies for the crawler. Please check `python-requests <http://docs.python-requests.org/en/master/user/quickstart/#cookies>`__ cookie jar for all the cookie options.

.. code:: python

    options.identity.cookies.set(name='tasty_cookie', value='yum', domain='finnwea.com', path='/cookies')

Proxy
~~~~~

Set a proxy for the crawler. Please check `python-requests <http://docs.python-requests.org/en/master/user/advanced/#proxies>`__ proxies for all the proxy options. Default is None (no proxy).

You can find examples of different types of proxies below.

.. code:: python

    # Without authentication
    options.identity.proxies = {
        'http': 'http://host:port',
        'https': 'http://host:port'
    }

    # With basic authentication
    options.identity.proxies = {
        'http': 'http://user:pass@host:port',
        'https': 'https://user:pass@host:port'
    }

    # With SOCKS
    options.identity.proxies = {
        'http': 'socks5://user:pass@host:port',
        'https': 'socks5://user:pass@host:port'
    }

Headers
~~~~~~~

Set custom headers for the crawler (as {key: value} CaseInsensitiveDict). For example, you can set a new user agent by using ``User-Agent`` as key, as shown below.

Please note that you should use the ``.update()`` method so the default headers remain the same.

.. code:: python

    options.identity.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36" # The user agent to make requests with.
    })
