"""
    Thin Layer Between Views and Provider Factory
"""
import random
import uuid
from datetime import datetime

from app.config import BNI_ECOLLECTION, BNI_RDL
from app.lib.core.remote_call import fetch
from app.lib.helper import encrypt


class BaseMockService:

    def __init__(self):
        self.transfer_info = None
        self.callback_payload = None
        self.va_info = None

    def set(self, transfer_info):
        self.transfer_info = transfer_info

    async def check_va(self):
        """ using virtual account no to look up into BNI dev serer """
        request = {
            "url": "http://dev.bni-ecollection.com/dev/flagging",
            "method": "POST",
            "headers": {
                "X-Requested-With": "XMLHttpRequest"
            },
            "data": {
                "va": self.transfer_info.destination
            }
        }
        response, status_code = await fetch(request)
        if response["code"] == 200:
            va_info = response["message"]
            self.va_info = va_info
            return True
        return False

    async def prepare_callback(self):
        """ build callback payload """
        payment_ntb = random.randint(111111, 999999)
        datetime_payment = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        callback_payload = {
            "virtual_account": self.va_info["virtual_account"],
            "customer_name": self.va_info["customer_name"],
            "trx_id": self.va_info["trx_id"],
            "trx_amount": "0",
            "payment_amount": self.transfer_info.amount,
            "cumulative_payment_amount": self.transfer_info.amount,
            "payment_ntb": str(payment_ntb),
            "datetime_payment": datetime_payment
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


class BniRdlMockService(BaseMockService):
    def generate_mock_response(self):
        """ using incoming parameter to generate mock response """
        journal_no = random.randint(111111, 999999)
        response_uuid = str(uuid.uuid4()).replace("-", "").upper()[:16]
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        mock_response = {
            "response": {
                "responseCode": "0001",
                "responseMessage": "Request has been processed successfully",
                "responseTimestamp": timestamp,
                "responseUuid": response_uuid,
                "journalNum": str(journal_no),
                "accountNumber": self.transfer_info.source,
                "beneficiaryAccountNumber": self.transfer_info.destination,
                "amount": self.transfer_info.amount,
            }
        }
        return mock_response


class BniOpgMockService(BaseMockService):
    def generate_mock_response(self):
        # if its BNI OPG use this mock response
        journal_no = random.randint(111111, 999999)
        timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

        mock_response = {
            "doPaymentResponse": {
                "clientId": "BNISERVICE",
                "parameters": {
                    "responseCode": "0001",
                    "responseMessage": "Request has been processed successfully",
                    "responseTimestamp": timestamp,
                    "debitAccountNo": self.transfer_info.source,
                    "creditAccountNo": self.transfer_info.destination,
                    "valueAmount": self.transfer_info.amount,
                    "valueCurrency": "IDR",
                    "bankReference": str(journal_no),
                    "customerReference": self.transfer_info.reference,
                },
            }
        }
        return mock_response

    async def generate_rdl_callback(self, account_no, amount):
        """ rdl callback for top up rdl """
        payment_ntb = random.randint(111111, 999999)
        datetime_payment = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        p2p_id = BNI_RDL["COMPANY"]
        callback_payload = {
            "p2p_id": p2p_id,
            "account_number": account_no,
            "payment_amount": amount,
            "accounting_flag": "C",
            "journal_number": str(payment_ntb),
            "datetime_payment": datetime_payment
        }

        encrypted_payload = encrypt(
            p2p_id,
            BNI_RDL["SECRET_API_KEY"],
            callback_payload,
        )

        data = {
            "client_id": p2p_id,
            "data": encrypted_payload,
        }
        return data
