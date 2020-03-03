import pytest


async def test_bni_auth_token(cli):
    headers = {
        "Authorization": "Basic ZWUyZDU0MDYtYmMyZC00YjMyLWExZDYtOWZmMDY4MTQ3ZjdhOjljOGM1ZWY3LTgwZTYtNGVhNS04YTczLTBmOTdkYTZmN2NkNg==",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {"grant_type": "client_credentials"}

    resp = await cli.post("/api/oauth/token", headers=headers, data=data)
    assert resp.status == 504
