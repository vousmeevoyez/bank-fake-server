"""
    BNI Rdl Auth Routes
    ______________________
    handle http request
"""
from aiohttp.web import View, json_response

from app.auth.services import get_token


class BniAuthView(View):
    """ Base class for forwarding view to services class """

    async def post(self):
        """ forward request to BNI to get auth Token """
        response, status_code = await get_token(self.request)
        return json_response(response, status=status_code)
