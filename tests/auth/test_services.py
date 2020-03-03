import json
import pytest
from asynctest import CoroutineMock, patch

from app.auth.services import get_token


@patch("aiohttp.ClientSession.request")
async def test_get_token_success(mock_request, make_aiohttp_request):
    """ test get token """
    expected_value = {
        "access_token": "x3LyfeWKbeaARhd2PfU4F4OeNi43CrDFdi6XnzScKIuk5VmvFiq0B2",
        "token_type": "Bearer",
        "expires_in": 3599,
        "scope": "resource.WRITE resource.READ",
    }

    mock_request.return_value.__aenter__.return_value.status = 200
    mock_request.return_value.__aenter__.return_value.text = CoroutineMock(
        return_value=json.dumps(expected_value)
    )

    headers = (
        (
            b"Authorization",
            b"Basic: ZWUyZDU0MDYtYmMyZC00YjMyLWExZDYtOWZmMDY4MTQ3ZjdhOjljOGM1ZWY3LTgwZTYtNGVhNS04YTczLTBmOTdkYTZmN2NkNg==",
        ),
        (b"Content-Type", b"application/x-www-form-urlencoded"),
    )
    data = {"grant_type": "client_credentials"}

    mock_request = make_aiohttp_request(
        headers=headers,
        data=data,
        url="/api/oauth/token",
        content_type="application/x-www-form-urlencoded",
        submit_type="post",
    )

    response, status_code = await get_token(mock_request)
    assert response["access_token"]
    assert response["token_type"]
    assert response["expires_in"]
    assert response["scope"]
    assert status_code == 200


@patch("aiohttp.ClientSession.request")
async def test_get_token_failed_but_mocked(mock_request, make_aiohttp_request):
    """ test get token """

    mock_request.return_value.__aenter__.return_value.status = 401
    mock_request.return_value.__aenter__.return_value.text = CoroutineMock(
        return_value=json.dumps(
            {
                "Response": {
                    "parameters": {
                        "responseCode": "0000",
                        "responseMessage": "Unknown output ",
                        "errorMessage": "Unknown output",
                    }
                }
            }
        )
    )

    headers = (
        (
            b"Authorization",
            b"Basic: ZWUyZDU0MDYtYmMyZC00YjMyLWExZDYtOWZmMDY4MTQ3ZjdhOjljOGM1ZWY3LTgwZTYtNGVhNS04YTczLTBmOTdkYTZmN2NkNg==",
        ),
        (b"Content-Type", b"application/x-www-form-urlencoded"),
    )
    data = {"grant_type": "client_credentials"}

    mock_request = make_aiohttp_request(
        headers=headers,
        data=data,
        url="/api/oauth/token",
        content_type="application/x-www-form-urlencoded",
        submit_type="post",
    )

    response, status_code = await get_token(mock_request)
    assert response["access_token"]
    assert response["token_type"]
    assert response["expires_in"]
    assert response["scope"]
    assert status_code == 200
