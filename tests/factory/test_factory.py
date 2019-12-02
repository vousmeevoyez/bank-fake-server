from app.services.factories.factory import (
    TransferInfo,
    generate_mock_service
)


def test_mock_service_rdl():
    transfer_info = TransferInfo(
        source="some-source-account",
        destination="9889909612795996",
        amount="10000",
        provider="BNI_RDL"
    )
    services = generate_mock_service(transfer_info)
    result = services.generate_mock_response()
    assert result["response"]


def test_mock_service_opg():
    transfer_info = TransferInfo(
        source="some-source-account",
        destination="9889909612795996",
        amount="10000",
        provider="BNI_OPG"
    )
    services = generate_mock_service(transfer_info)
    result = services.generate_mock_response()
    assert result["doPaymentResponse"]
