import pytest
from app.services.callback import generate_response_and_callback


@pytest.mark.asyncio
async def test_generate_response_and_callback_invalid_va():
    data = {
        "source": "some-source",
        "destination": "9889909612795996",
        "amount": "1000000",
        "provider": "BNI_RDL"
    }
    response = await generate_response_and_callback(**data)
    assert response

@pytest.mark.asyncio
async def test_generate_response_and_callback_valid_va():
    data = {
        "source": "some-source",
        "destination": "9889909611188474",
        "amount": "1000000",
        "provider": "BNI_RDL"
    }
    response = await generate_response_and_callback(**data)
    assert response
