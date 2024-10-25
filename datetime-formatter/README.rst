Example: datetime-formatter
===========================

.. code::

	# install dependencies in a poetry-managed virtualenv
	make install

	# start the proxy
	make start

This example demonstrate how the rules engine can be used to modify the content of a response on the fly. In this case, the response is a JSON object containing a timestamp. 
The applied rule will modify the date format to another common one (from ISO 8601 to RFC 2822).