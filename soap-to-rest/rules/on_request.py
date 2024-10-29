from harp.utils.bytes import ensure_bytes
from httpx import ByteStream
from harp.http import HttpRequest

# request will be defined in the context in which this code is executed
# cf https://docs.harp-proxy.net/en/0.7/apps/rules/on_request.html
request: HttpRequest

country_iso_code = request.query.get("sISOCode")
# XML template with a placeholder for the country ISO code
xml_template = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
    <soap:Body>
    <CountryCurrency xmlns="http://www.oorsprong.org/websamples.countryinfo">
        <sCountryISOCode>{country_iso_code}</sCountryISOCode>
    </CountryCurrency>
    </soap:Body>
</soap:Envelope>"""

new_path = "websamples.countryinfo/CountryInfoService.wso"
request.path = new_path

request.query = None
request.method = "POST"
request.headers.pop("content-length", None)
request.stream = ByteStream(ensure_bytes(xml_template))
