"""
    Thin Layer Between Views and Provider Factory
"""
from app.lib.services.products.base import BaseSerializedServices
from app.lib.callback.factory import trigger_callback


class CallbackServices(BaseSerializedServices):
    async def execute(self, resource):
        """ after receiving request, seriialized data and resource we trigger
        callback """
        await trigger_callback(self.request, resource, self.serialized_data)
