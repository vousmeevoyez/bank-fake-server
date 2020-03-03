from app.bni_opg.services import bni_inhouse_transfer


'''
async def test_opg_inhouse_transfer_to_va(make_aiohttp_request):
    headers = (
        (
            b"Authorization",
            b"Basic: ZWUyZDU0MDYtYmMyZC00YjMyLWExZDYtOWZmMDY4MTQ3ZjdhOjljOGM1ZWY3LTgwZTYtNGVhNS04YTczLTBmOTdkYTZmN2NkNg==",
        ),
        (b"Content-Type", b"application/x-www-form-urlencoded"),
    )
    data = {
        "customerReferenceNumber": "2020022806403750399681",
        "paymentMethod": "2",
        "debitAccountNo": "3571113886",
        "creditAccountNo": "1111222233334444",
        "valueDate": "20200228064058",
        "valueCurrency": "IDR",
        "valueAmount": 3996500,
        "remark": "?",
        "beneficiaryEmailAddress": "",
        "destinationBankCode": "CENAIDJAXXX",
        "beneficiaryName": "Beneficary name",
        "beneficiaryAddress1": "",
        "beneficiaryAddress2": "",
        "chargingModelId": "",
        "clientId": "IDBNITU9EQU5B",
        "signature": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0b21lclJlZmVyZW5jZU51bWJlciI6IjIwMjAwMjI4MDY0MDM3NTAzOTk2ODEiLCJwYXltZW50TWV0aG9kIjoiMiIsImRlYml0QWNjb3VudE5vIjoiMzU3MTExMzg4NiIsImNyZWRpdEFjY291bnRObyI6IjM3NTAwNTQ1MjciLCJ2YWx1ZURhdGUiOiIyMDIwMDIyODA2NDA1OCIsInZhbHVlQ3VycmVuY3kiOiJJRFIiLCJ2YWx1ZUFtb3VudCI6Mzk5NjUwMCwicmVtYXJrIjoiPyIsImJlbmVmaWNpYXJ5RW1haWxBZGRyZXNzIjoiIiwiZGVzdGluYXRpb25CYW5rQ29kZSI6IkNFTkFJREpBWFhYIiwiYmVuZWZpY2lhcnlOYW1lIjoiQW5uaXNhYSBadW5udXIgQWluaSIsImJlbmVmaWNpYXJ5QWRkcmVzczEiOiIiLCJiZW5lZmljaWFyeUFkZHJlc3MyIjoiIiwiY2hhcmdpbmdNb2RlbElkIjoiIiwiY2xpZW50SWQiOiJJREJOSVRVOUVRVTVCIn0.KdodwPGZOpL9V7fNNj3YqNU7o1-1rSlQh0DYzKUYWjc",
    }

    mock_request = make_aiohttp_request(
        headers=headers,
        data=data,
        url="/H2H/v2/dopayment",
        content_type="application/json",
        submit_type="json",
    )

    response, status_code = await bni_inhouse_transfer(mock_request)
    assert status_code == 200
    assert response["doPaymentResponse"]


async def test_opg_inhouse_transfer_to_rdl(make_real_aiohttp_request):
    """ simulate opg inhouse transfer to rdl account """
    headers = {
        "x-api-key": "some-api-key",
        "Content-Type": "application/json"
    }
    data = {
        "customerReferenceNumber": "2020022806403750399681",
        "paymentMethod": "2",
        "debitAccountNo": "3571113886",
        "creditAccountNo": "0317246673",
        "valueDate": "20200228064058",
        "valueCurrency": "IDR",
        "valueAmount": 3996500,
        "remark": "?",
        "beneficiaryEmailAddress": "",
        "destinationBankCode": "CENAIDJAXXX",
        "beneficiaryName": "Beneficary name",
        "beneficiaryAddress1": "",
        "beneficiaryAddress2": "",
        "chargingModelId": "",
        "clientId": "IDBNITU9EQU5B",
        "signature": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjdXN0b21lclJlZmVyZW5jZU51bWJlciI6IjIwMjAwMjI4MDY0MDM3NTAzOTk2ODEiLCJwYXltZW50TWV0aG9kIjoiMiIsImRlYml0QWNjb3VudE5vIjoiMzU3MTExMzg4NiIsImNyZWRpdEFjY291bnRObyI6IjM3NTAwNTQ1MjciLCJ2YWx1ZURhdGUiOiIyMDIwMDIyODA2NDA1OCIsInZhbHVlQ3VycmVuY3kiOiJJRFIiLCJ2YWx1ZUFtb3VudCI6Mzk5NjUwMCwicmVtYXJrIjoiPyIsImJlbmVmaWNpYXJ5RW1haWxBZGRyZXNzIjoiIiwiZGVzdGluYXRpb25CYW5rQ29kZSI6IkNFTkFJREpBWFhYIiwiYmVuZWZpY2lhcnlOYW1lIjoiQW5uaXNhYSBadW5udXIgQWluaSIsImJlbmVmaWNpYXJ5QWRkcmVzczEiOiIiLCJiZW5lZmljaWFyeUFkZHJlc3MyIjoiIiwiY2hhcmdpbmdNb2RlbElkIjoiIiwiY2xpZW50SWQiOiJJREJOSVRVOUVRVTVCIn0.KdodwPGZOpL9V7fNNj3YqNU7o1-1rSlQh0DYzKUYWjc",
    }

    mock_request = make_real_aiohttp_request(
        headers=headers,
        data=data,
        url="/H2H/v2/dopayment",
        method="POST"
    )

    response, status_code = await bni_inhouse_transfer(mock_request)
    assert status_code == 200
    assert response["doPaymentResponse"]
'''
