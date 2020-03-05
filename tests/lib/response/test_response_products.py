from app.lib.response.products import (
    BniRdlTransferSuccessResponse,
    BniRdlTransferFailedResponse,
    BniOpgTransferSuccessResponse,
    BniOpgTransferFailedResponse,
    OyVaSuccessResponse,
    OyVaFailedResponse,
)


def test_bni_rdl_successfull_fake_response():
    fake_response = BniRdlTransferSuccessResponse(
        {"source": "some-source", "destination": "some-destination", "amount": 1000}
    )
    response, status_code = fake_response.to_representation()
    assert status_code == 200
    assert response["response"]
    assert response["response"]["responseCode"]
    assert response["response"]["responseMessage"]
    assert response["response"]["responseTimestamp"]
    assert response["response"]["responseUuid"]
    assert response["response"]["journalNum"]
    assert response["response"]["accountNumber"] == "some-source"
    assert response["response"]["beneficiaryAccountNumber"] == "some-destination"
    assert response["response"]["amount"] == 1000
    # make sure the input passed to output


def test_bni_rdl_failed_fake_response():
    fake_response = BniRdlTransferFailedResponse(
        {"source": "some-source", "destination": "some-destination", "amount": 1000}
    )
    response, status_code = fake_response.to_representation()
    assert status_code == 500
    assert response["Response"]
    assert response["Response"]["parameters"]
    assert response["Response"]["parameters"]["responseCode"]
    assert response["Response"]["parameters"]["responseMessage"]
    assert response["Response"]["parameters"]["errorMessage"]


def test_bni_opg_successfull_fake_response():
    fake_response = BniOpgTransferSuccessResponse(
        {
            "source": "some-source",
            "destination": "some-destination",
            "amount": 1,
            "reference": "some-reference",
        }
    )
    response, status_code = fake_response.to_representation()
    assert status_code == 200
    assert response["doPaymentResponse"]
    assert response["doPaymentResponse"]["clientId"]
    assert response["doPaymentResponse"]["parameters"]
    assert response["doPaymentResponse"]["parameters"]["responseCode"]
    assert response["doPaymentResponse"]["parameters"]["responseMessage"]
    assert response["doPaymentResponse"]["parameters"]["responseTimestamp"]
    assert (
        response["doPaymentResponse"]["parameters"]["debitAccountNo"] == "some-source"
    )
    assert (
        response["doPaymentResponse"]["parameters"]["creditAccountNo"]
        == "some-destination"
    )
    assert response["doPaymentResponse"]["parameters"]["valueAmount"] == "1"
    assert response["doPaymentResponse"]["parameters"]["valueCurrency"]
    assert response["doPaymentResponse"]["parameters"]["bankReference"]
    assert response["doPaymentResponse"]["parameters"]["customerReference"]


def test_bni_opg_failed_fake_response():
    fake_response = BniOpgTransferFailedResponse(
        {"source": "some-source", "destination": "some-destination", "amount": 1000}
    )
    response, status_code = fake_response.to_representation()
    assert status_code == 500
    assert response["Response"]
    assert response["Response"]["parameters"]
    assert response["Response"]["parameters"]["responseCode"]
    assert response["Response"]["parameters"]["responseMessage"]
    assert response["Response"]["parameters"]["errorMessage"]


def test_oy_successfull_fake_response():
    fake_response = OyVaSuccessResponse({"amount": 1, "partner_user_id":
                                         "ABC123"})
    response, status_code = fake_response.to_representation()
    assert status_code == 200
    assert response["status"]
    assert response["status"]["code"]
    assert response["status"]["message"]
    assert response["amount"] == 1
    virtual_account = response["vaNumber"]
    assert virtual_account

    fake_response = OyVaSuccessResponse(
        {
            "amount": 100,
            "partner_user_id": "ABC123"
        }
    )
    response, status_code = fake_response.to_representation()
    assert status_code == 200
    assert response["status"]
    assert response["status"]["code"]
    assert response["status"]["message"]
    assert response["amount"] == 100
    assert response["vaNumber"] == virtual_account


def test_oy_failed_fake_response():
    fake_response = OyVaFailedResponse({"amount": 1})
    response, status_code = fake_response.to_representation()
    assert status_code == 200
    assert response["status"]
    assert response["status"]["code"]
    assert response["status"]["message"]
