from app.lib.core.factory import Factory
from app.services.factories.products import (
    BniRdlMockService,
    BniOpgMockService
)


class TransferInfo:

    def __init__(self, source, destination, amount, provider, currency=None,
                 remark=None, reference=None):
        self.provider = provider
        self.source = source
        self.destination = destination
        self.amount = amount
        self.currency = currency
        self.remark = remark
        self.reference = reference

    def load(self, generator):
        generator.set(self)


def generate_mock_service(transfer_info):
    factory = Factory()
    factory.register("BNI_RDL", BniRdlMockService)
    factory.register("BNI_OPG", BniOpgMockService)

    generator = factory.get(transfer_info.provider)
    transfer_info.load(generator)
    return generator
