"""
    Module responsible for faking response as if its generated from actual
    external server
"""
from app.lib.services.factory import generate_actual_services


async def oy_transfer(request):
    """ for oy we execute forward request and trigger a callback """
    services = await generate_actual_services(request, "FORWARD", "OY")
    response, status_code = await services.execute()

    callback_services = await generate_actual_services(request, "CALLBACK")
    if len(callback_services.serialized_data["destination"]) == 16:
        # trigger callback
        await callback_services.execute("BNI_VA")
    return response, status_code


async def generate_static_va(request):
    """ for oy we execute mock response """
    # we need to cache static va info and then re use it for updating
    services = await generate_actual_services(request, "FAKE")
    response, status_code = await services.execute()
    return response, status_code


async def update_static_va(request):
    """ for oy we execute mock response """
    services = await generate_actual_services(request, "FAKE")
    response, status_code = await services.execute()

    # get generated va_id
    va_id = request.match_info["id"]
    response["id"] = va_id
    return response, status_code
