from app.oy.services import (
    oy_transfer,
    generate_static_va
)


'''
async def test_oy_transfer(make_real_aiohttp_request):
    headers = {
        "X-OY-Username": "username",
        "X-Api-Key": "api-key",
    }
    data = {"recipient_bank": "014", "recipient_account": "1239812390"}

    mock_request = make_real_aiohttp_request(
        headers=headers,
        data=data,
        url="/api/remit",
        method="POST"
    )
    response, status_code = await oy_transfer(mock_request)
    print(response)
    print(status_code)
'''
