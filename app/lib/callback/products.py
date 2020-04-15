"""
    Thin Layer Between Views and Provider Factory
"""
import random
from datetime import datetime
from aiojobs.aiohttp import spawn

from app.jobs import trigger_callback
from app.lib.services.products.base import BaseSerializedServices
from app.lib.remote_call import fetch
from app.lib.helper import encrypt
from app.config import BNI_ECOLLECTION, BNI_RDL

from app.exceptions import VirtualAccountNotFoundError


class BaseCallback:
    def __init__(self, request, serialized_data):
        self.request = request
        self.serialized_data = serialized_data

    async def prepare(self):
        """ prepare something before actually executing callback """
        return self.serialized_data

    async def trigger(self):
        """ mostly we use this for generating fake response and triggering
        callback """
        callback_payload = await self.prepare()
        await spawn(self.request, trigger_callback(callback_payload))


class BniVaCallback(BaseCallback):
    async def check_va(self, va_no):
        """ using virtual account no to look up into BNI dev serer """
        request = {
            "url": "http://dev.bni-ecollection.com/dev/flagging",
            "method": "POST",
            "headers": {"X-Requested-With": "XMLHttpRequest"},
            "data": {"va": va_no},
        }
        response, status_code = await fetch(request)
        if response["code"] == 200:
            va_info = response["message"]
            return True, va_info
        return False, {}

    async def prepare(self):
        """ build callback payload """
        payment_ntb = random.randint(111111, 999999)
        datetime_payment = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        is_valid, va_info = await self.check_va(self.serialized_data["destination"])
        if not is_valid:
            raise VirtualAccountNotFoundError

        callback_payload = {
            "virtual_account": va_info["virtual_account"],
            "customer_name": va_info["customer_name"],
            "trx_id": va_info["trx_id"],
            "trx_amount": "0",
            "payment_amount": self.serialized_data["amount"],
            "cumulative_payment_amount": self.serialized_data["amount"],
            "payment_ntb": str(payment_ntb),
            "datetime_payment": datetime_payment,
        }

        encrypted_payload = encrypt(
            BNI_ECOLLECTION["CREDIT_CLIENT_ID"],
            BNI_ECOLLECTION["CREDIT_SECRET_KEY"],
            callback_payload,
        )

        data = {
            "client_id": BNI_ECOLLECTION["CREDIT_CLIENT_ID"],
            "data": encrypted_payload,
        }
        return data

    async def trigger(self):
        """ mostly we use this for generating fake response and triggering
        callback """
        try:
            callback_payload = await self.prepare()
        except VirtualAccountNotFoundError:
            pass
            # do nothing
        else:
            await spawn(self.request, trigger_callback(callback_payload))


class BniRdlCallback(BaseCallback):
    async def prepare(self):
        """ rdl callback for top up rdl """
        payment_ntb = random.randint(111111, 999999)
        datetime_payment = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        p2p_id = BNI_RDL["COMPANY"]
        callback_payload = {
            "p2p_id": p2p_id,
            "account_number": self.serialized_data["destination"],
            "payment_amount": self.serialized_data["amount"],
            "accounting_flag": "C",
            "journal_number": str(payment_ntb),
            "datetime_payment": datetime_payment,
        }

        encrypted_payload = encrypt(p2p_id, BNI_RDL["SECRET_API_KEY"], callback_payload)

        data = {"client_id": p2p_id, "data": encrypted_payload}
        return data
