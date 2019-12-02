"""
    Thin Layer Between Views and Provider Factory
"""
from aiojobs.aiohttp import spawn

from app.lib.core.exceptions import BaseError
from app.services.factories.factory import TransferInfo, generate_mock_service
from app.jobs import trigger_callback


async def generate_response_and_callback(source, destination, amount, provider,
                                         currency=None, remark=None,
                                         reference=None, request=None):
    transfer_info = TransferInfo(
        source=source, destination=destination,
        amount=amount, provider=provider,
        currency=currency, remark=remark,
        reference=reference
    )
    mock_services = generate_mock_service(transfer_info)
    response = mock_services.generate_mock_response()
    if len(destination) == 16:
        is_valid = await mock_services.check_va()
        if is_valid:
            callback_payload = await mock_services.prepare_callback()
            await spawn(request, trigger_callback(callback_payload))
    # if its rdl should trigger something
    elif destination[1] == "3":
        callback_payload = await mock_services.generate_rdl_callback(
            destination,
            amount
        )
        await spawn(request, trigger_callback(callback_payload))

    return response
