from app.serializer import BniRdlTransferSchema, BniOpgTransferSchema


def test_serialize():
    data = {
        "request": {
            "header": {
                "signature": "some-signature-long",
                "companyId": "SANDBOX",
                "parentCompanyId": "STI_CHS",
                "requestUuid": "E8C6E0027F6E429F"
            },
                "accountNumber": "0115476117",
                "beneficiaryAccountNumber": "0115471119",
                "currency": "IDR",
                "amount": "11500",
                "remark": "Test P2PL"
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
        "chargingModelId": "OUR"
    }

    result = BniOpgTransferSchema().dump(data)
    assert result["source"] == "113183203"
    assert result["destination"] == "115471119"
    assert result["currency"] == "IDR"
    assert result["amount"] == "100500"
    assert result["remark"] == "?"
    assert result["reference"] == "20170227000000000020"
