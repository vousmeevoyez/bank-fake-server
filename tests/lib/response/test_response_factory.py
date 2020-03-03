"""
from app.lib.response.factory import generate_fake_response
from app.routes import ROUTER


def test_bni_rdl_generate_fake_response():
    fake_response, status_code = generate_fake_response(
        ROUTER["BNI_RDL_INHOUSE_TRF"],
        {"source": "some-source", "destination": "some-destination", "amount": 1},
    )
    assert fake_response["response"]
    assert fake_response["response"]["responseCode"]
    assert fake_response["response"]["responseMessage"]
    assert fake_response["response"]["responseTimestamp"]
    assert fake_response["response"]["responseUuid"]
    assert fake_response["response"]["journalNum"]
    assert fake_response["response"]["accountNumber"] == "some-source"
    assert fake_response["response"]["beneficiaryAccountNumber"] \
        == "some-destination"
    assert fake_response["response"]["amount"] == 1
    assert status_code == 200


def test_bni_opg_generate_fake_response():
    fake_response, status_code = generate_fake_response(
        ROUTER["BNI_OPG_INHOUSE_TRF"],
        {
            "source": "some-source",
            "destination": "some-destination",
            "amount": 1,
            "reference": "some-reference",
        },
    )
    assert fake_response["doPaymentResponse"]
    assert fake_response["doPaymentResponse"]["clientId"]
    assert fake_response["doPaymentResponse"]["parameters"]
    assert fake_response["doPaymentResponse"]["parameters"]["responseCode"]
    assert fake_response["doPaymentResponse"]["parameters"]["responseMessage"]
    assert fake_response["doPaymentResponse"]["parameters"]["responseTimestamp"]
    assert fake_response["doPaymentResponse"]["parameters"]["debitAccountNo"]\
        == "some-source"
    assert fake_response["doPaymentResponse"]["parameters"]["creditAccountNo"]\
        == "some-destination"
    assert fake_response["doPaymentResponse"]["parameters"]["valueAmount"]\
        == 1
    assert fake_response["doPaymentResponse"]["parameters"]["valueCurrency"]
    assert fake_response["doPaymentResponse"]["parameters"]["bankReference"]
    assert fake_response["doPaymentResponse"]["parameters"]["customerReference"]
    assert status_code == 200

    fake_response, status_code = generate_fake_response(
        ROUTER["OY_GENERATE_VA"], {"amount": 1}
    )
    assert fake_response["status"]
    assert fake_response["status"]["code"]
    assert fake_response["status"]["message"]
    assert fake_response["amount"] == 1
    assert fake_response["vaNumber"]
    assert status_code == 200
"""
