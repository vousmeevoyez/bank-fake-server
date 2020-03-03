import pytest
import asyncio
from unittest.mock import Mock

from aiohttp.test_utils import make_mocked_request
from app.lib.services.products.forwarder import ForwarderServices


@pytest.mark.asyncio
async def test_forward_request(make_aiohttp_request):
    headers = ((b"X-OY-Username", b"modana"), (b"X-Api-Key", b"dev-oykey-modana"))
    data = {"recipient_bank": "014", "recipient_account": "1239812390"}
    mocked = make_aiohttp_request(data=data, headers=headers, url="/api/inquiry")

    services = await ForwarderServices.create(mocked, "OY")
    response, status_code = await services.execute()
    assert status_code == 200
    assert response
