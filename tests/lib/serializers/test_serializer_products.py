from decimal import Decimal
from app.lib.serializers.products import (
    BniRdlTransferSchema,
    BniOpgTransferSchema,
    OyStaticVaSchema,
    OyUpdateStaticVaSchema,
)
from app.routes import ROUTER


def test_serialize():
    data = {
        "request": {
            "header": {
                "signature": "some-signature-long",
                "companyId": "SANDBOX",
                "parentCompanyId": "STI_CHS",
                "requestUuid": "E8C6E0027F6E429F",
            },
            "accountNumber": "0115476117",
            "beneficiaryAccountNumber": "0115471119",
            "currency": "IDR",
            "amount": "11500",
            "remark": "Test P2PL",
        }
    }

    result = BniRdlTransferSchema().dump(data)
    assert result["source"] == "0115476117"
    assert result["destination"] == "0115471119"
    assert result["currency"] == "IDR"
    assert result["amount"] == "11500"
    assert result["remark"] == "Test P2PL"

    data = {
        "clientId": "smoeclientid",
        "signature": "somesignature",
        "customerReferenceNumber": "20170227000000000020",
        "paymentMethod": "0",
        "debitAccountNo": "113183203",
        "creditAccountNo": "115471119",
        "valueDate": "20170227000000000",
        "valueCurrency": "IDR",
        "valueAmount": "100500",
        "remark": "?",
        "beneficiaryEmailAddress": "",
        "beneficiaryName": "Mr .X",
        "beneficiaryAddress1": "Jakarta",
        "beneficiaryAddress2": "",
        "destinationBankCode": "CENAIDJAXXX",
        "chargingModelId": "OUR",
    }

    result = BniOpgTransferSchema().dump(data)
    assert result["source"] == "113183203"
    assert result["destination"] == "115471119"
    assert result["currency"] == "IDR"
    assert result["amount"] == "100500"
    assert result["remark"] == "?"
    assert result["reference"] == "20170227000000000020"

    data = {
        "partner_user_id": "oy00000001",
        "bank_code": "002",
        "amount": 500000,
        "is_open": False,
        "is_single_use": True,
        "is_lifetime": True,
        "expiration_time": "",
        "username_display": "",
    }
    result = OyStaticVaSchema().dump(data)
    assert result["amount"] == Decimal("500000")
    assert result["partner_user_id"] == "oy00000001"
    assert result["bank_code"] == "002"
    assert result["is_open"] is False
    assert result["is_single_use"] is True
    assert result["is_lifetime"] is True
    assert result["expiration_time"] == ""
    assert result["username_display"] == ""

    data = {
        "amount": 500001,
        "is_open": True,
        "is_single_use": True,
        "is_lifetime": True,
        "expiration_time": "",
    }
    result = OyUpdateStaticVaSchema().dump(data)
    assert result["amount"] == Decimal("500001")
    assert result["is_open"] is True
    assert result["is_single_use"] is True
    assert result["is_lifetime"] is True
    assert result["expiration_time"] == ""
