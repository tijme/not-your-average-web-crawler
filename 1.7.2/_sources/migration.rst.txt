.. title:: Migration

From 1.6 to 1.7
---------------

.. raw:: html

    <p><code>pip install --upgrade nyawc</code></p><br>

**Default request timeout is now 30 seconds**

From now on there is a default request timeout of 30 seconds. In previous versions it was always infinite and you couldn't specify it.

If you want to keep the request timeout on infinite set the request timeout option to ``None``.

.. code:: python

    options.performance.request_timeout = 30

**Count attributes removed from queue**

The count attributes (e.g. ``queue.count_in_progress``) are removed since the time complexity of Python's native ``len()`` method is already O(n).

.. code:: python

    # Old
    print("In progress count: " + str(queue.count_in_progress))

    # New
    print("In progress count: " + str(len(queue.get_all(QueueItem.STATUS_IN_PROGRESS))))

From 1.5 to 1.6
---------------

.. raw:: html

    <p><code>pip install --upgrade nyawc</code></p><br>

**Headers have default values and are case insensitive**

From now on the headers identity option has default values and is a case insensitive dict. When changing headers the ``.update()`` method should be used so the default headers remain the same.

.. code:: python

    # Old
    options.identity.headers = {
        "User-Agent": "MyCustomUserAgent"
    }

    # New
    options.identity.headers.update({
        "User-Agent": "MyCustomUserAgent"
    })

**New default user agent**

The default user agent for the crawler has changed. In version 1.5 it was a fake Chrome user agent and from now on it is ``nyawc/1.6.0 CPython/3.6.1 Windows/10`` based on the versions you use.

The Chrome user agent from version 1.5 can still be faked by using the code below.

.. code:: python

    options.identity.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    })

From 1.4 to 1.5
---------------

.. raw:: html

    <p><code>pip install --upgrade nyawc</code></p><br>

**Renamed the domain must match scope option**

Since version 1.5 the domain_must_match option is now called hostname_must_match.

.. code:: python

    # Old
    Options().scope.domain_must_match = True/False

    # New
    Options().scope.hostname_must_match = True/False
