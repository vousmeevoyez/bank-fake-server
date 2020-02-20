"""
    Excute Async HTTP Call
    ____________________
"""
import logging
import json
import aiohttp

from app.lib.core.exceptions import BaseError
from app.logger import logger as fetch_logger


class FetchError(BaseError):
    """ raised when aiohttp error """


async def fetch(request):
    """ async call using request and response """
    fetch_logger.setLevel(logging.INFO)

    async with aiohttp.ClientSession() as session:
        fetch_logger.info("REQUEST: {}".format(request))
        try:
            async with session.request(**request) as resp:
                response = await resp.text()
                try:
                    response = json.loads(response)
                except json.decoder.JSONDecodeError:
                    pass

                if resp.content_type == "application/json":
                    response = await resp.json(content_type=None)

                fetch_logger.info("STATUS CODE: {}".format(resp.status))
                fetch_logger.info("RESPONSE: {}".format(response))
                status = resp.status
        except aiohttp.ClientError as exc:
            response = {"message": str(exc)}
            return response, 500
        else:
            return response, status
