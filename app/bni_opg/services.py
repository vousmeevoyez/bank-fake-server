"""
    Module responsible for faking response as if its generated from actual
    external server
"""
from app.lib.services.factory import generate_actual_services


async def bni_inhouse_transfer(request):
    """
        fake incoming request with OPG Inhouse transfer fake response and
        trigger callback
    """
    services = await generate_actual_services(request, "FAKE")
    response, status_code = await services.execute()

    callback_services = await generate_actual_services(request, "CALLBACK")
    if len(services.serialized_data["destination"]) == 16:
        # trigger callback
        await callback_services.execute("BNI_VA")
    elif services.serialized_data["destination"][1] == "3":
        await callback_services.execute("BNI_RDL")
    return response, status_code
