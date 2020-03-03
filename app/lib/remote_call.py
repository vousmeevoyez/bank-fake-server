"""
    Excute Async HTTP Call
    ____________________
"""
import logging
import json
import aiohttp

from app.exceptions import FetchError
from app.logger import logger as fetch_logger


async def fetch(request):
    """ async call using request and response """
    fetch_logger.setLevel(logging.INFO)

    async with aiohttp.ClientSession() as session:
        fetch_logger.info("REQUEST: {}".format(request))
        try:
            async with session.request(**request) as resp:
                # if json we access it directly
                if resp.content_type == "application/json":
                    response = await resp.json(content_type=None)
                else:
                    response = await resp.text()
                    try:
                        response = json.loads(response)
                    except json.decoder.JSONDecodeError:
                        pass

                fetch_logger.info("STATUS CODE: {}".format(resp.status))
                fetch_logger.info("RESPONSE: {}".format(response))
                status = resp.status
        except aiohttp.ClientError as exc:
            response = {"message": str(exc)}
            return response, 500
        else:
            return response, status
