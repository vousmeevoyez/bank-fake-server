from app.bni_rdl.views import *
from app.bni_opg.views import *
from app.oy.views import *
from app.auth.views import *


ROUTER = {
    "BNI_OAUTH": "/api/oauth/token",
    "BNI_RDL_REGISTER": "/p2pl/register/investor",
    "BNI_RDL_REGISTER_ACC": "/p2pl/register/investor/account",
    "BNI_RDL_ACC_INFO": "/p2pl/inquiry/account/info",
    "BNI_RDL_ACC_BALANCE": "/p2pl/inquiry/account/balance",
    "BNI_RDL_ACC_HISTORY": "/p2pl/inquiry/account/history",
    "BNI_RDL_INHOUSE_TRF": "/p2pl/payment/transfer",
    "BNI_RDL_PAYMENT_INQUIRY": "/p2pl/inquiry/payment/status",
    "BNI_RDL_CLEARING_TRF": "/p2pl/payment/clearing",
    "BNI_RDL_RTGS_TRF": "/p2pl/payment/rtgs",
    "BNI_RDL_INTERBANK_INQUIRY": "/p2pl/inquiry/interbank/account",
    "BNI_RDL_INTERBANK_TRF": "/p2pl/payment/interbank",
    # OPG
    "BNI_OPG_ACC_BALANCE": "/H2H/v2/getbalance",
    "BNI_OPG_ACC_INQUIRY": "/H2H/v2/getinhouseinquiry",
    "BNI_OPG_INHOUSE_TRF": "/H2H/v2/dopayment",
    "BNI_OPG_PAYMENT_INQUIRY": "/H2H/v2/getpaymentstatus",
    "BNI_OPG_INTERBANK_INQUIRY": "/H2H/v2/getinterbankinquiry",
    "BNI_OPG_INTERBANK_TRF": "/H2H/v2/getinterbankpayment",
    # OY
    "OY_INQUIRY": "/api/inquiry",
    "OY_INTERBANK_TRF": "/api/remit",
    "OY_PAYMENT_INQUIRY": "/api/remit-status",
    "OY_BALANCE": "/api/balance",
    "OY_GENERATE_VA": "/api/generate-static-va",
}


def setup_routes(app):
    # RDL
    app.router.add_view(ROUTER["BNI_OAUTH"], BniAuthView)
    app.router.add_view(ROUTER["BNI_RDL_REGISTER"], BniRdLRegisterView)
    app.router.add_view(ROUTER["BNI_RDL_REGISTER_ACC"], BniRdLRegisterAccountView)
    app.router.add_view(ROUTER["BNI_RDL_ACC_INFO"], BniRdlAccountInfoView)
    app.router.add_view(ROUTER["BNI_RDL_ACC_BALANCE"], BniRdlAccountBalanceView)
    app.router.add_view(ROUTER["BNI_RDL_ACC_HISTORY"], BniRdlAccountHistoryView)
    app.router.add_view(ROUTER["BNI_RDL_INHOUSE_TRF"], BniRdlInhouseTransferView)
    app.router.add_view(ROUTER["BNI_RDL_PAYMENT_INQUIRY"], BniRdlInquiryPaymentView)
    app.router.add_view(ROUTER["BNI_RDL_CLEARING_TRF"], BniRdlClearingTransferView)
    app.router.add_view(ROUTER["BNI_RDL_RTGS_TRF"], BniRdlRtgsTransferView)
    app.router.add_view(ROUTER["BNI_RDL_INTERBANK_INQUIRY"], BniRdlInterbankAccountView)
    app.router.add_view(ROUTER["BNI_RDL_INTERBANK_TRF"], BniRdlInterbankTransferView)
    # OPG
    app.router.add_view(ROUTER["BNI_OPG_ACC_BALANCE"], BniOpgAccountBalanceView)
    app.router.add_view(ROUTER["BNI_OPG_ACC_INQUIRY"], BniOpgAccountInfoView)
    app.router.add_view(ROUTER["BNI_OPG_INHOUSE_TRF"], BniOpgInhouseTransferView)
    app.router.add_view(ROUTER["BNI_OPG_PAYMENT_INQUIRY"], BniOpgTransferInquiryView)
    app.router.add_view(ROUTER["BNI_OPG_INTERBANK_INQUIRY"], BniOpgInterbankInquiryView)
    app.router.add_view(ROUTER["BNI_OPG_INTERBANK_TRF"], BniOpgInterbankTransferView)
    # OY
    app.router.add_view(ROUTER["OY_INQUIRY"], OyAccountInquiryView)
    app.router.add_view(ROUTER["OY_INTERBANK_TRF"], OyDisburseView)
    app.router.add_view(ROUTER["OY_PAYMENT_INQUIRY"], OyDisburseStatusView)
    app.router.add_view(ROUTER["OY_BALANCE"], OyBalanceView)
    app.router.add_view(ROUTER["OY_GENERATE_VA"], OyStaticVaView)
