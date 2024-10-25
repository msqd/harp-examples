Example: circuit breaker
====================

.. code::

	# install dependencies in a poetry-managed virtualenv
	make install

	# start the proxy
	make start

Example: circuit breaker
====================

.. code::

    # install dependencies in a poetry-managed virtualenv
    make install

    # start the proxy
    make start

This example implements a circuit breaker with harp.
The proxy is configured so that it will break the circuit on HTTP 4xx, HTTP 5xx, or network errors. It will check the remote endpoints every 5 seconds only when the circuit is open (i.e., when the primary endpoint is down).
The configuration includes a fallback mechanism. If the primary endpoint (`https://httpbin.org`) fails, the proxy will attempt to use the fallback endpoint (`http://httpbin.org`). This ensures higher availability and reliability of the service.
For more information about the proxy settings, please refer to the `Harp Proxy Settings Documentation <https://docs.harp-proxy.net/en/latest/apps/proxy/settings.html>`_.