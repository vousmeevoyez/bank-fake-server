from app.lib.core.factory import Factory
from app.lib.serializers.products import (
    BniRdlTransferSchema,
    BniOpgTransferSchema,
    OyStaticVaSchema,
    OyDisburseSchema
)


def generate_serializer(rel_url):
    """ we generate serializer based on incoming request path """
    from app.routes import ROUTER

    factory = Factory()
    factory.register(ROUTER["BNI_RDL_INHOUSE_TRF"], BniRdlTransferSchema)
    factory.register(ROUTER["BNI_OPG_INHOUSE_TRF"], BniOpgTransferSchema)
    factory.register(ROUTER["OY_GENERATE_VA"], OyStaticVaSchema)
    factory.register(ROUTER["OY_INTERBANK_TRF"], OyDisburseSchema)

    choosen_factory = factory.get(rel_url)
    return choosen_factory


async def generate_serialized_data(request):
    """ after receiving incoming request we generate the correct serializer and
    then return the serializied data """
    serializer = generate_serializer(request.path)

    json_data = await request.json()
    serialized_data = serializer().dump(json_data)
    return serialized_data
