"""
    Module responsible for faking response as if its generated from actual
    external server
    this is connected with fake response factory
"""

from app.lib.services.products.base import BaseSerializedServices
from app.lib.response.factory import generate_fake_response


class FakeServices(BaseSerializedServices):
    """ generate fake services """

    async def execute(self, is_success=True):
        """ override class execute with generating fake response from fake
        response factory """
        response, status_code = generate_fake_response(
            self.request.path, self.serialized_data, is_success
        )
        return response, status_code
