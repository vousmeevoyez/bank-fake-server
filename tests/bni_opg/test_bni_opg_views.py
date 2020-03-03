import pytest
import json


async def test_opg_inhouse_transfer(cli):
    headers = {
        "Authorization": "Basic ZWUyZDU0MDYtYmMyZC00YjMyLWExZDYtOWZmMDY4MTQ3ZjdhOjljOGM1ZWY3LTgwZTYtNGVhNS04YTczLTBmOTdkYTZmN2NkNg==",
        "Content-Type": "application/json",
    }
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
    url = "/H2H/v2/dopayment?access_token=someaccesstoken"

    resp = await cli.post(url, headers=headers, data=json.dumps(data))
    assert resp.status == 200
    response = json.loads(await resp.text())
    assert response["doPaymentResponse"]
