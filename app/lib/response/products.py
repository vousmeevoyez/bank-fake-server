"""
    Handle Serialization from BNI RDL And OPG
"""
import json
import uuid
from random import randint
from datetime import datetime

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
            "randomint": str(randint(111111, 999999))
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
        "amount": $amount,\
        "vaNumber": "$vaNumber"\
    }'

    def generate_static_data(self):
        start_range = "1" * 16
        end_range = "9" * 16

        static_data = {
            "vaNumber": randint(int(start_range), int(end_range))
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
