"""
    BNI Rdl Auth Routes
    ______________________
    handle http request
"""
from aiohttp import web

from app.services.forwarder import forward_request


class BniAuthView(web.View):
    """ Base class for forwarding view to services class """

    async def post(self):
        """ forward request to BNI to get auth Token """
        response, status_code = await forward_request(
            relative_url=self.request.rel_url,
            headers=self.request.raw_headers,
            request=self.request,
        )
        # if its error try again once with BNI OPG
        if status_code == 401:
            response, status_code = await forward_request(
                relative_url=self.request.rel_url,
                headers=self.request.raw_headers,
                request=self.request,
                resource="BNI_OPG"
            )

        return web.json_response(response, status=status_code)
