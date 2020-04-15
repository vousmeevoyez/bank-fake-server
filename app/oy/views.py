"""
    BNI Rdl Auth Routes
    ______________________
    handle http request
"""
from aiohttp import web

from app.lib.services.factory import generate_actual_services
from app.oy.services import oy_transfer, generate_static_va, update_static_va


class BaseForwardView(web.View):
    """ Base class for forwarding view to services class """

    async def post(self):
        """ we post the request to external service and generate callback """
        services = await generate_actual_services(self.request, "FORWARD", "OY")
        response, status_code = await services.execute()
        return web.json_response(response, status=status_code)

    async def get(self):
        """ we forward request to external services """
        services = await generate_actual_services(self.request, "FORWARD", "OY")
        response, status_code = await services.execute()
        return web.json_response(response, status=status_code)


class OyAccountInquiryView(BaseForwardView):
    """ oy bank account inquiry view """


class OyDisburseView(BaseForwardView):
    """ oy send money / remit view """

    async def post(self):
        """ extend base forward POST method and trigger callback """
        response, status_code = await oy_transfer(self.request)
        return web.json_response(response, status=status_code)


class OyDisburseStatusView(BaseForwardView):
    """ oy disburse status view """


class OyBalanceView(BaseForwardView):
    """ oy balance view """


class OyStaticVaView(BaseForwardView):
    """ oy generate static va view """

    async def post(self):
        """ extend base forward POST method and trigger callback """
        response, status_code = await generate_static_va(self.request)
        return web.json_response(response, status=status_code)


class OyVaDetailsView(BaseForwardView):
    """ Handle OY VA Detail View """

    async def put(self):
        """ extend base forward POST method and trigger callback """
        response, status_code = await update_static_va(self.request)
        return web.json_response(response, status=status_code)
