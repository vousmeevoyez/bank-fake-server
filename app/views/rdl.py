"""
    BNI Rdl Auth Routes
    ______________________
    handle http request
"""
import ast
from aiohttp import web
from aiohttp_apispec import request_schema


from app.serializer import BniRdlTransferSchema
from app.services.forwarder import forward_request
from app.services.callback import generate_response_and_callback


class BaseForwardView(web.View):
    """ Base class for forwarding view to services class """

    async def post(self):
        """ forward request to BNI to get auth Token """
        response, status_code = await forward_request(
            relative_url=self.request.rel_url,
            headers=self.request.raw_headers,
            request=self.request,
        )
        return web.json_response(response, status=status_code)


class BniRdlInhouseTransferView(web.View):
    """ BNI RDL Inhouse transfer View """

    async def post(self):
        """ mock bni response and trigger callback """
        request_data = await self.request.json()
        serialized_data = BniRdlTransferSchema().dump(request_data)
        serialized_data["request"] = self.request

        response = await generate_response_and_callback(**serialized_data)
        return web.json_response(response)


class BniRdLAuthView(BaseForwardView):
    """ BNI RDL Authentication View """


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
