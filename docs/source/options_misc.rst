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
    options.misc.verify_ssl_certificates = True
    options.misc.trusted_certificates = None

    crawler = Crawler(options)
    crawler.start_with(Request("https://finnwea.com/"))

Available misc options
----------------------

Debug
~~~~~

If debug is enabled extra information will be logged to the console. Default is False.

``options.misc.debug = True``


Verify SSL certificates
~~~~~~~~~~~~~~~~~~~~~~~

If verification is enabled all SSL certificates will be checked for validity. Default is True.

``options.misc.verify_ssl_certificates = True``


Trusted certificates
~~~~~~~~~~~~~~~~~~~~

To trust certain certificates (e.g. if you are using a proxy), you can pass the path to a CA_BUNDLE file or directory with certificates of additional trusted CAs. Default is None (which means only domains with valid SSL certificates can be crawled).

**If verify is set to a path to a directory, the directory must have been processed using the c_rehash utility supplied with OpenSSL.**

``options.misc.trusted_certificates = '/path/to/certificate.pem'``
