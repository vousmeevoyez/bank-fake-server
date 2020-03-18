"""
    Handle Serialization from BNI RDL And OPG
"""
import json
import uuid
import functools

from random import randint
from datetime import datetime, timedelta

from string import Template


class BaseResponse:

    status_code = 200
    templates = '{\
        "responseCode": "0001",\
        "responseMessage": "Request has been processed successfully",\
        "responseTimestamp": "$timestamp",\
        "responseUuid": "$uuid",\
        "journalNum": "$randomint",\
        "accountNumber": "$source",\
        "beneficiaryAccountNumber": "$destination",\
        "amount": $amount\
    }'

    def __init__(self, serialized_data):
        self.serialized_data = serialized_data

    def generate_static_data(self):
        static_data = {
            "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
            "uuid": str(uuid.uuid4()).replace("-", "").upper()[:16],
            "randomint": str(randint(111111, 999999)),
        }
        return static_data

    def to_representation(self):
        t = Template(self.templates)
        # merge serialized + static data
        static_data = self.generate_static_data()
        merged_dict = {**self.serialized_data, **static_data}
        response = t.safe_substitute(**merged_dict)
        return json.loads(response), self.status_code


class BniRdlTransferSuccessResponse(BaseResponse):
    """ represent BNI RDl INHOUSE TRANSFER Success Response """

    templates = '{\
            "response": {\
                "responseCode": "0001",\
                "responseMessage": "Request has been processed successfully",\
                "responseTimestamp": "$timestamp",\
                "responseUuid": "$uuid",\
                "journalNum": "$randomint",\
                "accountNumber": "$source",\
                "beneficiaryAccountNumber": "$destination",\
                "amount": $amount\
            }\
    }'


class BniRdlTransferFailedResponse(BaseResponse):
    """ represent BNI RDl INHOUSE TRANSFER Failed Response """

    status_code = 500
    templates = '{\
      "Response": {\
        "parameters": {\
          "responseCode": "0000",\
          "responseMessage": "Unknown output ",\
          "errorMessage": "Unknown output"\
        }\
      }\
    }'


class BniOpgTransferSuccessResponse(BaseResponse):
    """ represent BNI OPG INHOUSE TRANSFER Success Response """

    templates = '{\
        "doPaymentResponse": {\
            "clientId": "BNISERVICE",\
            "parameters": {\
                "responseCode": "0001",\
                "responseMessage": "Request has been processed successfully",\
                "responseTimestamp": "$timestamp",\
                "debitAccountNo": "$source",\
                "creditAccountNo": "$destination",\
                "valueAmount": "$amount",\
                "valueCurrency": "IDR",\
                "bankReference": "$randomint",\
                "customerReference": "$reference"\
            }\
        }\
    }'


class BniOpgTransferFailedResponse(BaseResponse):
    """ represent BNI OPG INHOUSE TRANSFER Failed Response """

    status_code = 500
    templates = '{\
        "Response": {\
            "parameters": {\
                "responseCode": "0000",\
                "responseMessage": "Unknown output ",\
                "errorMessage": "Unknown output"\
            }\
        }\
    }'


class OyVaSuccessResponse(BaseResponse):
    """ represent OY Generate static va success Response """

    templates = '{\
        "status": {\
            "code": "000",\
            "message": "Success"\
        },\
        "id": "$uuid",\
        "amount": $amount,\
        "va_number": "$va_number",\
        "bank_code": "$bank_code",\
        "is_open": $converted_is_open,\
        "is_single_use": $converted_is_single_use,\
        "expiration_time": $expiration_time,\
        "va_status": "$va_status",\
        "username_display": "$username_display"\
    }'

    @staticmethod
    def str2int(chars):
        result = ""
        for char in chars:
            result += str(ord(char))
        return result

    def generate_virtual_account(self, serialized_data):
        """ generate virtual account no """
        partner_user_id = serialized_data["partner_user_id"]
        va_length = 16

        converted_str = self.str2int(partner_user_id)
        return converted_str[:va_length]

    def generate_expiration_time(self, serialized_data):
        # check if lifetime is true then we return expiration time as -1 to
        # indiicate it active indefinitely
        # by default expriation time is 24 hour from now
        day_from_now = datetime.utcnow() + timedelta(hours=24)
        expiration_time = day_from_now.timestamp()

        is_lifetime = serialized_data["is_lifetime"]
        if is_lifetime:
            expiration_time = -1
        return expiration_time

    def convert_py_bool_to_js(self, serialized_data):
        # because some encoding issue we can't use True or False directly
        is_open = serialized_data["is_open"]
        converted_is_open = "false"
        if is_open:
            converted_is_open = "true"

        is_single_use = self.serialized_data["is_single_use"]
        converted_is_single_use = "false"
        if is_single_use:
            converted_is_single_use = "true"
        return converted_is_open, converted_is_single_use

    def generate_static_data(self):
        virtual_account = self.generate_virtual_account(self.serialized_data)

        expiration_time = self.generate_expiration_time(self.serialized_data)

        is_open, is_single_use = \
            self.convert_py_bool_to_js(self.serialized_data)

        static_data = {
            "va_number": int(virtual_account),
            "va_status": "WAITING_PAYMENT",
            "uuid": str(uuid.uuid4()),
            "expiration_time": expiration_time,
            "username_display": "MODANA",
            "converted_is_open": is_open,
            "converted_is_single_use": is_single_use,
        }
        return static_data


class OyUpdateVaSuccessResponse(OyVaSuccessResponse):
    """ represent OY Generate static va success Response """

    # we only return dynamic information here because the info that can't be
    # update will retrieved later by cache
    templates = '{\
        "status": {\
            "code": "000",\
            "message": "Success"\
        },\
        "amount": $amount,\
        "is_open": $converted_is_open,\
        "is_single_use": $converted_is_single_use,\
        "expiration_time": $expiration_time,\
        "username_display": "$username_display"\
    }'

    def generate_static_data(self):
        expiration_time = self.generate_expiration_time(self.serialized_data)

        is_open, is_single_use = \
            self.convert_py_bool_to_js(self.serialized_data)

        static_data = {
            "expiration_time": expiration_time,
            "username_display": "MODANA",
            "converted_is_open": is_open,
            "converted_is_single_use": is_single_use,
        }
        return static_data


class OyVaFailedResponse(BaseResponse):
    """ represent OY Generate static va success Response """

    templates = '{\
        "status": {\
            "code": "999",\
            "message": "Internal Server Error"\
        }\
    }'
