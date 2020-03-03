from app.lib.core.factory import Factory
from app.lib.services.products.callback import CallbackServices
from app.lib.services.products.forwarder import ForwarderServices
from app.lib.services.products.mocker import FakeServices


def generate_services(type_):
    """ we generate serializer based on incoming request path """
    factory = Factory()
    factory.register("CALLBACK", CallbackServices)
    factory.register("FORWARD", ForwarderServices)
    factory.register("FAKE", FakeServices)
    return factory.get(type_)


async def generate_actual_services(request, type_, resource=None):
    services = generate_services(type_)
    actual_services = await services.create(request)
    if resource is not None:
        actual_services = await services.create(request, resource)
    return actual_services
