"""
    Thin Layer Between Views and Provider Factory
"""
import aiohttp

from app.lib.services.products.base import BaseServices

from app.config import LOGGING, FORWARD_CONFIG
from app.lib.remote_call import fetch


class ForwarderServices(BaseServices):

    request = None
    resource = None

    @classmethod
    async def create(cls, request, resource=None):
        """ factory method wrapped in async to create forwarder services """
        self = cls()
        self.request = request
        self.resource = resource
        return self

    def unpack_headers(self):
        """ convert raw headers into dictionary """
        headers = {}
        for key, value in self.request.raw_headers:
            decoded_key = key.decode("utf-8")
            decoded_value = value.decode("utf-8")
            if decoded_key != "Host":
                headers[decoded_key] = decoded_value
        return headers

    def unpack_payload(self, payload):
        """ used to convert non json payload into dictionary """
        data = {}
        for key, value in payload.items():
            data[key] = value
        return data

    async def unpack_request(self):
        """ convert request payload into either json or dictionary post so it
        can be requested to server """
        key = "json"
        if self.request.content_type == "application/json":
            payload = await self.request.json()
        else:
            key = "data"
            payload = await self.request.post()
            payload = self.unpack_payload(payload)
        return payload, key

    async def execute(self):
        """ forward the received request to designated resource backend """
        # forwarded url
        forwarded_url = FORWARD_CONFIG[self.resource] \
            + str(self.request.rel_url)
        # prepare all information here
        data, key = await self.unpack_request()
        headers = self.unpack_headers()

        request = {
            "method": self.request.method,
            "url": forwarded_url,
            "headers": headers,
            "timeout": aiohttp.ClientTimeout(total=LOGGING["TIMEOUT"]),
        }
        # assign request body either to json or post form here
        request[key] = data

        response, status_code = await fetch(request)
        return response, status_code
