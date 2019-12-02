import pytest
import json
from asynctest import CoroutineMock, patch

async def test_get_rdl_token(cli):
    headers = {
        "Authorization": "Basic ZWUyZDU0MDYtYmMyZC00YjMyLWExZDYtOWZmMDY4MTQ3ZjdhOjljOGM1ZWY3LTgwZTYtNGVhNS04YTczLTBmOTdkYTZmN2NkNg==",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {'grant_type': 'client_credentials'}

    resp = await cli.post('/api/oauth/token', headers=headers, data=data)
    assert resp.status == 504


async def test_bni_rdl_inhouse_transfer(cli):
    headers = {
        "x-api-key": "7e6e5c9d-ed58-4a98-be46-434c5a8f2792",
        "Content-Type": "application/json"
    }
    data = {
        "request": {
            "header": {
                "signature": "some-signature-long",
                "companyId": "SANDBOX",
                "parentCompanyId": "STI_CHS",
                "requestUuid": "E8C6E0027F6E429F"
            },
                "accountNumber": "0115476117",
                "beneficiaryAccountNumber": "9889909669787085",
                "currency": "IDR",
                "amount": "11500",
                "remark": "Test P2PL"
            }
    }

    url = "/p2pl/payment/transfer?access_token=someaccesstoken"
    resp = await cli.post(url, headers=headers, data=json.dumps(data))
    assert resp.status == 200
