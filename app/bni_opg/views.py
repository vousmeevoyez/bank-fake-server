"""
    BNI Rdl Auth Routes
    ______________________
    handle http request
"""
from aiohttp import web

from app.lib.services.factory import generate_actual_services
from app.bni_opg.services import bni_inhouse_transfer


class BaseForwardView(web.View):
    """ Base class for forwarding view to services class """

    async def post(self):
        """ forward request to BNI to get auth Token """
        services = await generate_actual_services(
            self.request,
            "FORWARD",
            "BNI_OPG"
        )
        response, status_code = await services.execute()
        return web.json_response(response, status=status_code)


class BniOpgInhouseTransferView(web.View):
    """ BNI OPG Inhouse transfer View """

    async def post(self):
        """ mock bni response and trigger callback """
        response, status_code = await bni_inhouse_transfer(self.request)
        return web.json_response(response, status=status_code)


class BniOpgAccountInfoView(BaseForwardView):
    """ BNI RDL Register Account Info View """


class BniOpgAccountBalanceView(BaseForwardView):
    """ BNI RDL Register Account Balance View """


class BniOpgTransferInquiryView(BaseForwardView):
    """ BNI RDL Register Account History View """


class BniOpgInterbankInquiryView(BaseForwardView):
    """ BNI RDL interbank account inquiry View """


class BniOpgInterbankTransferView(BaseForwardView):
    """ BNI RDL interbank transfer View """
