"""
    Thin Layer Between Views and Provider Factory
"""
import aiohttp
from datetime import datetime

from app.config import LOGGING, FORWARD_CONFIG
from app.lib.core.remote_call import fetch


def unpack_headers(raw_headers):
    """ convert raw headers into dictionary """
    headers = {}
    for key, value in raw_headers:
        decoded_key = key.decode("utf-8")
        decoded_value = value.decode("utf-8")
        if decoded_key != "Host":
            headers[decoded_key] = decoded_value
    return headers


def unpack_payload(payload):
    """ convert raw headers into dictionary """
    data = {}
    for key, value in payload.items():
        data[key] = value
    return data


async def unpack_request(request):
    """ convert raw headers into dictionary """
    key = "json"
    if request.content_type == "application/json":
        payload = await request.json()
    else:
        key = "data"
        payload = await request.post()
        payload = unpack_payload(payload)
    return payload, key


async def forward_request(
    relative_url, headers, request, method="POST", resource="BNI_RDL"
):
    """ forward the received request to actual backend """
    # forwarded url
    forwarded_url = FORWARD_CONFIG[resource] + str(relative_url)
    # request payload
    data, key = await unpack_request(request)
    request = {
        "method": method,
        "url": forwarded_url,
        "headers": unpack_headers(headers),
        "timeout": aiohttp.ClientTimeout(total=LOGGING["TIMEOUT"]),
    }
    # assign request here
    request[key] = data

    response, status_code = await fetch(request)
    return response, status_code
