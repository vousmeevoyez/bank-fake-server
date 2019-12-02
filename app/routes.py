from app.views.rdl import *
from app.views.opg import *
from app.views.auth import BniAuthView


def setup_routes(app):
    # RDL
    app.router.add_view("/api/oauth/token", BniAuthView)
    app.router.add_view("/p2pl/register/investor", BniRdLRegisterView)
    app.router.add_view("/p2pl/register/investor/account", BniRdLRegisterAccountView)
    app.router.add_view("/p2pl/inquiry/account/info", BniRdlAccountInfoView)
    app.router.add_view("/p2pl/inquiry/account/balance", BniRdlAccountBalanceView)
    app.router.add_view("/p2pl/inquiry/account/history", BniRdlAccountHistoryView)
    app.router.add_view("/p2pl/payment/transfer", BniRdlInhouseTransferView)
    app.router.add_view("/p2pl/inquiry/payment/status", BniRdlInquiryPaymentView)
    app.router.add_view("/p2pl/payment/clearing", BniRdlClearingTransferView)
    app.router.add_view("/p2pl/payment/rtgs", BniRdlRtgsTransferView)
    app.router.add_view("/p2pl/inquiry/interbank/account", BniRdlInterbankAccountView)
    app.router.add_view("/p2pl/payment/interbank", BniRdlInterbankTransferView)
    # OPG
    app.router.add_view("/H2H/v2/getbalance", BniOpgAccountBalanceView)
    app.router.add_view("/H2H/v2/getinhouseinquiry", BniOpgAccountInfoView)
    app.router.add_view("/H2H/v2/dopayment", BniOpgInhouseTransferView)
    app.router.add_view("/H2H/v2/getpaymentstatus", BniOpgTransferInquiryView)
    app.router.add_view("/H2H/v2/getinterbankinquiry", BniOpgInterbankInquiryView)
    app.router.add_view("/H2H/v2/getinterbankpayment", BniOpgInterbankTransferView)
