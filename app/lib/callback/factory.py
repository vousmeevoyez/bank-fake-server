from app.lib.core.factory import Factory
from app.lib.callback.products import (
    BniVaCallback,
    BniRdlCallback
)


def generate_callback(resource):
    """ we generate serializer based on incoming request path """

    factory = Factory()
    factory.register("BNI_VA", BniVaCallback)
    factory.register("BNI_RDL", BniRdlCallback)

    choosen_factory = factory.get(resource)
    return choosen_factory


async def trigger_callback(request, resource, serialized_data):
    callback = generate_callback(resource)
    await callback(request, serialized_data).trigger()
