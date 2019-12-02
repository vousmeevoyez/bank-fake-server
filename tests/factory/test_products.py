import pytest
import json
from unittest.mock import Mock
from asynctest import CoroutineMock, patch

from app.services.factories.products import BaseMockService


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request")
async def test_mock_service_valid_va(mock_request):
    expected_value = {
        'code': 200,
        'message': {
            'trx_id': '664285884',
            'billing_type': 'o',
            'trx_amount': '',
            'virtual_account': '9889909612795996',
            'customer_name': 'Investment for 5dcca0a71bcdd4f653f9799e',
            'currency': 'IDR'
        },
        'nominal_only': 1
    }

    mock_request.return_value.__aenter__.return_value.status = 200
    mock_request.return_value.__aenter__.return_value.text = CoroutineMock(
            return_value=json.dumps(expected_value)
    )

    transfer_info = Mock(
        source="some-bank-account",
        destination="9889909612795996",
        amount="10000",
        provider="BNI_RDL",
    )
    mock_services = BaseMockService()
    mock_services.set(transfer_info)
    result = await mock_services.check_va()
    assert result
    assert mock_services.va_info["virtual_account"] == "9889909612795996"


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request")
async def test_mock_service_invalid_va(mock_request):
    expected_value = {'code': 404, 'message': 'Invalid VA number.'}

    mock_request.return_value.__aenter__.return_value.status = 200
    mock_request.return_value.__aenter__.return_value.text = CoroutineMock(
            return_value=json.dumps(expected_value)
    )

    transfer_info = Mock(
        source="some-bank-account",
        destination="1111111111111111",
        amount="10000",
        provider="BNI_RDL",
    )
    mock_services = BaseMockService()
    mock_services.set(transfer_info)
    result = await mock_services.check_va()
    assert result is False


@pytest.mark.asyncio
@patch("aiohttp.ClientSession.request")
async def test_mock_service_build_callback(mock_request):
    expected_value = {
        'code': 200,
        'message': {
            'trx_id': '664285884',
            'billing_type': 'o',
            'trx_amount': '',
            'virtual_account': '9889909612795996',
            'customer_name': 'Investment for 5dcca0a71bcdd4f653f9799e',
            'currency': 'IDR'
        },
        'nominal_only': 1
    }

    mock_request.return_value.__aenter__.return_value.status = 200
    mock_request.return_value.__aenter__.return_value.text = CoroutineMock(
            return_value=json.dumps(expected_value)
    )

    transfer_info = Mock(
        source="some-bank-account",
        destination="9889909612795996",
        amount="10000",
        provider="BNI_RDL",
    )
    mock_services = BaseMockService()
    mock_services.set(transfer_info)
    await mock_services.check_va()
    payload = await mock_services.prepare_callback()
    assert payload["client_id"]
    assert payload["data"]
