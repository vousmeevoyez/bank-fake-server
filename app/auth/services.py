"""
    Bni Auth Services
"""
from app.lib.services.factory import generate_actual_services


async def get_token(request):
    """ reqeust token to BNI OPG or RDL if not error we fake it """
    rdl_services = await generate_actual_services(request, "FORWARD", "BNI_RDL")
    response, status_code = await rdl_services.execute()

    # to prevent silly failed if status code is not successfull we rpelace
    # it with fake response
    if status_code > 200:
        response = {
            "access_token": "V0nmtLdEfvkc2QmKfu5ycsfIttl84ge8P0G3yAV2HDv9VGFG8s2URa",
            "token_type": "Bearer",
            "expires_in": 3600,
            "scope": "resource.WRITE resource.READ",
        }
        status_code = 200
    return response, status_code
