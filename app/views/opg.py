"""
    BNI Rdl Auth Routes
    ______________________
    handle http request
"""
import ast
from aiohttp import web

from app.serializer import BniOpgTransferSchema
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
            resource="BNI_OPG",
        )
        return web.json_response(response, status=status_code)


class BniOpgInhouseTransferView(web.View):
    """ BNI OPG Inhouse transfer View """

    async def post(self):
        """ mock bni response and trigger callback """
        request_data = await self.request.json()
        serialized_data = BniOpgTransferSchema().dump(request_data)
        serialized_data["request"] = self.request

        response = await generate_response_and_callback(**serialized_data)
        return web.json_response(response)


class BniOpgAuthView(BaseForwardView):
    """ BNI RDL Authentication View """


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
