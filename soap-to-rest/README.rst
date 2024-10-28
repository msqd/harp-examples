Example: soap-to-rest
=====================
This project demonstrates how to transform a SOAP request into a RESTful GET request using **Harp Proxy rules**. The transformation allows a client to make a REST call to a specific endpoint with query parameters, which the proxy then translates into a SOAP request. The SOAP response is converted to JSON for RESTful responses.

**SOAP Endpoint**
- Base URL: ``http://webservices.oorsprong.org``
- Path: ``/websamples.countryinfo/CountryInfoService.wso``

The following example explains the transformation of a SOAP request into a RESTful GET request.

.. code::

	# install dependencies in a poetry-managed virtualenv
	make install

	# start the proxy
	make start



Overview
========

The original SOAP request for retrieving a country's currency information is structured as follows:

.. code-block:: python

    xml_template = f"""<?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
          <sCountryISOCode>{country_iso_code}</sCountryISOCode>
        </CountryCurrency>
      </soap:Body>
    </soap:Envelope>"""

This SOAP request sends the ``sCountryISOCode`` as a parameter within the XML body. Using Harp Proxy, we convert this into a RESTful GET request by changing the path and adding ``sISOCode`` as a query parameter. 

REST Transformation
===================

After transformation, the SOAP request is replaced with a RESTful GET request that uses a query parameter for the country code. The new request format looks like this:

**RESTful GET Request**
- URL: ``http://localhost:<proxy_port>``
- Query Parameter: ``?sISOCode=<country_iso_code>``

Example REST GET request::

    http://localhost:<proxy_port>?sISOCode=US

Response Transformation
=======================

The original SOAP response is in XML format and resembles the following structure:

.. code-block:: xml

    <?xml version="1.0" encoding="utf-8"?>
    <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
        <soap:Body>
            <m:CountryCurrencyResponse xmlns:m="http://www.oorsprong.org/websamples.countryinfo">
                <m:CountryCurrencyResult>
                    <m:sISOCode>USD</m:sISOCode>
                    <m:sName>Dollars</m:sName>
                </m:CountryCurrencyResult>
            </m:CountryCurrencyResponse>
        </soap:Body>
    </soap:Envelope>

Using Harp Proxy rules, the response is converted to JSON, allowing a RESTful response structure as shown below:

.. code-block:: json

    {
        "CountryCurrencyResponse": {
            "CountryCurrencyResult": {
                "sISOCode": "USD",
                "sName": "Dollars"
            }
        }
    }

This JSON structure makes it easier to work with data in REST applications, especially when handling errors or missing data.


Usage
=====

1. Run Harp Proxy with the appropriate rules to handle SOAP to REST transformations.
2. Make a GET request to the transformed RESTful endpoint with the query parameter ``sISOCode`` for the desired country code.
3. The response will be returned in JSON format, suitable for RESTful clients.

For more information on setting up Harp Proxy, refer to the documentation at https://harp-proxy.net.
