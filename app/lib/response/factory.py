"""
    Fake response factory modules
"""
from os.path import split
from app.lib.core.factory import Factory
from app.lib.response.products import (
    BniOpgTransferSuccessResponse,
    BniRdlTransferSuccessResponse,
    OyVaSuccessResponse,
    OyUpdateVaSuccessResponse,
    # BniOpgTransferFailedResponse,
    # BniRdlTransferFailedResponse,
    # OyVaFailedResponse,
)


def generate_fake_response(url_path, serialized_data, is_success=True):
    """ we generate serializer based on incoming request path """
    from app.routes import ROUTER

    factory = Factory()
    # if is success response we generate from this factory
    factory.register(ROUTER["BNI_RDL_INHOUSE_TRF"], BniRdlTransferSuccessResponse)
    factory.register(ROUTER["BNI_OPG_INHOUSE_TRF"], BniOpgTransferSuccessResponse)
    factory.register(ROUTER["OY_GENERATE_VA"], OyVaSuccessResponse)
    factory.register(ROUTER["OY_VA_DETAILS"], OyUpdateVaSuccessResponse)

    try:
        selected_factory = factory.get(url_path)
    except ValueError:
        splitted_path = split(url_path)
        selected_factory = factory.get(splitted_path[0] + "/{id}")
    # end try
    return selected_factory(serialized_data).to_representation()
