Example: basic setup
====================

.. code:: shell

	# install dependencies in a poetry-managed virtualenv
	make install

	# start the proxy, using a builtin example provided (proxy:httpbin)
	make start

* http://[::]:4000 is the proxied httpbin
* http://[::]:4080 is the HARP dashboard
