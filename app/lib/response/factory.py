"""
    Fake response factory modules
"""
from app.lib.core.factory import Factory
from app.lib.response.products import (
    BniOpgTransferSuccessResponse,
    BniRdlTransferSuccessResponse,
    OyVaSuccessResponse,
    BniOpgTransferFailedResponse,
    BniRdlTransferFailedResponse,
    OyVaFailedResponse
)


def generate_fake_response(url_path, serialized_data, is_success=True):
    """ we generate serializer based on incoming request path """
    from app.routes import ROUTER

    factory = Factory()
    # if is success response we generate from this factory
    if is_success:
        factory.register(
            ROUTER["BNI_RDL_INHOUSE_TRF"], BniRdlTransferSuccessResponse
        )
        factory.register(
            ROUTER["BNI_OPG_INHOUSE_TRF"], BniOpgTransferSuccessResponse
        )
        factory.register(
            ROUTER["OY_GENERATE_VA"], OyVaSuccessResponse
        )
    # if not success response we generate from this factory
    else:
        factory.register(
            ROUTER["BNI_RDL_INHOUSE_TRF"], BniRdlTransferFailedResponse
        )
        factory.register(
            ROUTER["BNI_OPG_INHOUSE_TRF"], BniOpgTransferFailedResponse
        )
        factory.register(
            ROUTER["OY_GENERATE_VA"], OyVaFailedResponse
        )

    selected_factory = factory.get(url_path)
    return selected_factory(serialized_data).to_representation()
