import pytest
from aiohttp.test_utils import make_mocked_request

from app.lib.callback.products import BniRdlCallback, BniVaCallback
from app.exceptions import VirtualAccountNotFoundError


@pytest.mark.asyncio
async def test_bni_va_callback_success(decode_encrypted_response):
    request = make_mocked_request("GET", "/", headers={"token": "access-token"})
    callback_response = await BniVaCallback(
        request, {"destination": "9889909681279926", "amount": 1000}
    ).prepare()
    # make sure its valid response
    assert callback_response["client_id"]
    assert callback_response["data"]
    # make sure its right decrypted response
    decrypted_response = decode_encrypted_response(callback_response)
    assert decrypted_response["virtual_account"]
    assert decrypted_response["customer_name"]
    assert decrypted_response["trx_id"]
    assert decrypted_response["trx_amount"]
    assert decrypted_response["payment_amount"]
    assert decrypted_response["cumulative_payment_amount"]
    assert decrypted_response["payment_ntb"]
    assert decrypted_response["datetime_payment"]


@pytest.mark.asyncio
async def test_bni_va_callback_failed(decode_encrypted_response):
    request = make_mocked_request("GET", "/", headers={"token": "access-token"})
    with pytest.raises(VirtualAccountNotFoundError):
        await BniVaCallback(
            request, {"destination": "9889900000000", "amount": 1000}
        ).prepare()


@pytest.mark.asyncio
async def test_bni_rdl_callback_success(decode_encrypted_response):
    request = make_mocked_request("GET", "/", headers={"token": "access-token"})
    callback_response = await BniRdlCallback(
        request, {"destination": "some-rdl-destination", "amount": 1000}
    ).prepare()
    # make sure its valid response
    assert callback_response["client_id"]
    assert callback_response["data"]
    # make sure its right decrypted response
    decrypted_response = decode_encrypted_response(callback_response)
    assert decrypted_response["p2p_id"]
    assert decrypted_response["account_number"]
    assert decrypted_response["payment_amount"]
    assert decrypted_response["accounting_flag"]
    assert decrypted_response["journal_number"]
    assert decrypted_response["datetime_payment"]
