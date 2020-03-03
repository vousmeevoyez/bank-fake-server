"""
    Thin Layer Between Views and Provider Factory
"""
import random
from datetime import datetime
from aiojobs.aiohttp import spawn

from app.jobs import trigger_callback
from app.lib.remote_call import fetch
from app.lib.helper import encrypt
from app.config import BNI_ECOLLECTION

from app.lib.serializers.factory import generate_serialized_data
from app.exceptions import VirtualAccountNotFoundError


class BaseServices:

    request = None

    @classmethod
    async def create(cls, request):
        """ use this because __int__ doesn't work with async """
        self = cls()
        self.request = request
        return self

    async def execute(self):
        pass


class BaseSerializedServices(BaseServices):
    """
        this class used for services that rely on serialiized data and request
    """

    request = None
    serialized_data = None

    @classmethod
    async def create(cls, request):
        """ factory method wrapped in async to create forwarder services """
        self = cls()
        self.request = request
        self.serialized_data = await generate_serialized_data(request)
        return self
