import asyncio
import pytest
from aiohttp import web

from unittest.mock import Mock
from aiohttp.test_utils import make_mocked_request
from aiojobs.aiohttp import setup as aiojobs_setup


from app import register_routes
from app.config import BNI_ECOLLECTION, BNI_RDL
from app.lib.helper import decrypt


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    register_routes(app)
    aiojobs_setup(app)
    return loop.run_until_complete(aiohttp_client(app))


@pytest.fixture
def make_aiohttp_request():
    def _make_aiohttp_request(
        headers,
        data,
        url,
        content_type="application/json",
        method="POST",
        submit_type="json",
    ):
        @asyncio.coroutine
        def submitted_data():
            return data

        mocked = Mock()
        mocked.content_type = content_type
        setattr(mocked, submit_type, submitted_data)
        mocked.raw_headers = headers
        mocked.method = method
        mocked.rel_url = url
        mocked.path = url
        return mocked

    return _make_aiohttp_request


@pytest.fixture
def make_real_aiohttp_request():
    def _make_real_aiohttp_request(headers, data, url, method):
        mocked = make_mocked_request(method, url, headers=headers, payload=data)
        return mocked

    return _make_real_aiohttp_request


@pytest.fixture
def decode_encrypted_response():
    """ decode BNI VA or RDL REsponse"""

    def _decode_encrypted_response(response):
        if response["client_id"] == BNI_RDL["COMPANY"]:
            decrypted_payload = decrypt(
                BNI_RDL["COMPANY"], BNI_RDL["SECRET_API_KEY"], response["data"]
            )
        else:
            decrypted_payload = decrypt(
                BNI_ECOLLECTION["CREDIT_CLIENT_ID"],
                BNI_ECOLLECTION["CREDIT_SECRET_KEY"],
                response["data"],
            )
        return decrypted_payload

    return _decode_encrypted_response
