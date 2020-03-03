import pytest
import asyncio
from unittest.mock import Mock

from app.lib.serializers.factory import generate_serialized_data


@pytest.mark.asyncio
async def test_generate_serialized_data(make_aiohttp_request):
    headers = ((b"X-OY-Username", b"modana"), (b"X-Api-Key", b"dev-oykey-modana"))
    data = {"partner_user_id": "oy00000001", "bank_code": "002", "amount": 500000}

    mocked = make_aiohttp_request(
        data=data, headers=headers, url="/api/generate-static-va"
    )

    serialized_data = await generate_serialized_data(mocked)
    assert serialized_data["amount"]
    assert serialized_data["bank_code"]
    assert serialized_data["partner_user_id"]
