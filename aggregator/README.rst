Example: aggregator
===================

.. code::

	# install dependencies in a poetry-managed virtualenv
	make install

	# start the proxy
	make start

You can then combine httbin/uuid and httpbin2/cookies using the aggregator.
with the following command:

.. code::
	curl --location 'http://localhost:4070/combine' 
