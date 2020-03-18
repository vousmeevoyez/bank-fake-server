import pytest
import asyncio
from unittest.mock import Mock

from aiohttp.test_utils import make_mocked_request, make_mocked_coro
from app.lib.services.products.mocker import FakeServices


@pytest.mark.asyncio
async def test_oy_fake_request(make_aiohttp_request):
    mocked = make_aiohttp_request(
        data={
            "partner_user_id": "oy00000001",
            "bank_code": "002",
            "amount": 500000,
            "is_open": False,
            "is_single_use": True,
            "is_lifetime": True,
            "expiration_time": "",
            "username_display": "",
        },
        headers=((b"X-OY-Username", b"modana"), (b"X-Api-Key", b"dey-oykey-modana")),
        url="/api/generate-static-va",
        method="POST",
    )

    services = await FakeServices.create(mocked)
    response, status_code = await services.execute()
    assert status_code == 200
    assert response["status"]
    assert response["status"]["code"]
    assert response["status"]["message"]
    assert response["id"]
    assert response["amount"] == 500000
    assert response["is_open"] is False
    assert response["is_single_use"] is True
    assert response["expiration_time"] == -1
    assert response["username_display"] == "MODANA"


@pytest.mark.asyncio
async def test_bni_opg_fake_request(make_aiohttp_request):
    data = {
        "clientId": "IDBNICLIENTID",
        "signature": "somesignature",
        "customerReferenceNumber": "20170227000000000020",
        "paymentMethod": "0",  # 0 IN_HOUSE // 1 RTGS // 3 CLEARING
        "debitAccountNo": "113183203",  # registered BNI account
        "creditAccountNo": "115471119",  # destination BNI / EXTERNAL BANK
        "valueDate": "20170227000000000",  # yyyyMMddHHmmss
        "valueCurrency": "IDR",  # IDR
        "valueAmount": "100500",
        "remark": "?",
        "beneficiaryEmailAddress": "",  # must be filled if not IN_HOUSE
        "destinationBankCode": "",  # must be filled if not IN_HOUSE
        "beneficiaryName": "Mr. K",  # must be filled if not IN_HOUSE
        "beneficiaryAddress1": "Jakarta",
        "beneficiaryAddress2": "",
        "chargingModelId": "",  # whos pay for it (OUR/BEN/SHA)
    }
    mocked = make_aiohttp_request(
        data=data,
        headers=(
            (b"Content-Type", b"application/json"),
            (b"X-api-key", b"bni-api-key"),
        ),
        url="/H2H/v2/dopayment",
        method="POST",
    )

    services = await FakeServices.create(mocked)
    response, status_code = await services.execute()
    assert status_code == 200
    assert response["doPaymentResponse"]
    assert response["doPaymentResponse"]["clientId"]
    assert response["doPaymentResponse"]["parameters"]
    assert response["doPaymentResponse"]["parameters"]["responseCode"]
    assert response["doPaymentResponse"]["parameters"]["responseMessage"]
    assert response["doPaymentResponse"]["parameters"]["responseTimestamp"]
    assert response["doPaymentResponse"]["parameters"]["debitAccountNo"]
    assert response["doPaymentResponse"]["parameters"]["creditAccountNo"]
    assert response["doPaymentResponse"]["parameters"]["valueAmount"]
    assert response["doPaymentResponse"]["parameters"]["valueCurrency"]
    assert response["doPaymentResponse"]["parameters"]["bankReference"]
    assert response["doPaymentResponse"]["parameters"]["customerReference"]


@pytest.mark.asyncio
async def test_bni_rdl_fake_request(make_aiohttp_request):
    data = {
        "request": {
            "header": {
                "signature": "some-signature-long",
                "companyId": "SANDBOX",
                "parentCompanyId": "STI_CHS",
                "requestUuid": "E8C6E0027F6E429F",
            },
            "accountNumber": "0115476117",
            "beneficiaryAccountNumber": "9889909669787085",
            "currency": "IDR",
            "amount": "11500",
            "remark": "Test P2PL",
        }
    }
    mocked = make_aiohttp_request(
        data=data,
        headers=(
            (b"Content-Type", b"application/json"),
            (b"X-api-key", b"bni-api-key"),
        ),
        url="/p2pl/payment/transfer",
        method="POST",
    )

    services = await FakeServices.create(mocked)
    response, status_code = await services.execute()
    assert status_code == 200
    assert response["response"]
    assert response["response"]["responseCode"]
    assert response["response"]["responseMessage"]
    assert response["response"]["responseTimestamp"]
    assert response["response"]["responseUuid"]
    assert response["response"]["journalNum"]
    assert response["response"]["accountNumber"]
    assert response["response"]["beneficiaryAccountNumber"]
    assert response["response"]["amount"]
