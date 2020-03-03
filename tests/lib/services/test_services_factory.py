from app.lib.services.factory import generate_services
from app.lib.services.products.forwarder import ForwarderServices
from app.lib.services.products.mocker import FakeServices


def test_generate_services():
    services = generate_services("FORWARD")

    services = generate_services("FAKE")
