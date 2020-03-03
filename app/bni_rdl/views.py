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
            "BNI_RDL"
        )
        response, status_code = await services.execute()
        return web.json_response(response, status=status_code)


class BniRdlInhouseTransferView(web.View):
    """ BNI RDL Inhouse transfer View """

    async def post(self):
        """ mock bni response and trigger callback """
        response, status_code = await bni_inhouse_transfer(self.request)
        return web.json_response(response, status=status_code)


class BniRdLRegisterView(BaseForwardView):
    """ BNI RDL Register Investor View """


class BniRdLRegisterAccountView(BaseForwardView):
    """ BNI RDL Register Account View """


class BniRdlAccountInfoView(BaseForwardView):
    """ BNI RDL Register Account Info View """


class BniRdlAccountBalanceView(BaseForwardView):
    """ BNI RDL Register Account Balance View """


class BniRdlAccountHistoryView(BaseForwardView):
    """ BNI RDL Register Account History View """


class BniRdlInquiryPaymentView(BaseForwardView):
    """ BNI RDL Inquiry Payment View """


class BniRdlClearingTransferView(BaseForwardView):
    """ BNI RDL clearing transfer View """


class BniRdlRtgsTransferView(BaseForwardView):
    """ BNI RDL RTGS Transfer View """


class BniRdlInterbankAccountView(BaseForwardView):
    """ BNI RDL interbank account inquiry View """


class BniRdlInterbankTransferView(BaseForwardView):
    """ BNI RDL interbank transfer View """
