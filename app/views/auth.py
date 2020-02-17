"""
    BNI Rdl Auth Routes
    ______________________
    handle http request
"""
from aiohttp import web

from app.services.forwarder import forward_request
from app.services.factories.product import generate_fake_token


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

        # to prevent silly failed if status code is not successfull we rpelace
        # it with fake response
        if status_code > 200:
            response, status_code = generate_fake_token()
        return web.json_response(response, status=status_code)
