"""
    Handle Serialization from BNI RDL And OPG
"""
from datetime import datetime
from marshmallow import Schema, fields, EXCLUDE, post_dump, ValidationError


class BniRdlInnerSchema(Schema):
    source = fields.Str(attribute="accountNumber")
    destination = fields.Str(attribute="beneficiaryAccountNumber")
    currency = fields.Str()
    amount = fields.Str()
    remark = fields.Str()
    reference = fields.Str()


class BniRdlTransferSchema(Schema):
    """ schema used for transfer using BNI RDL """

    request = fields.Nested(BniRdlInnerSchema())

    class Meta:
        unknown = EXCLUDE

    @post_dump
    def custom_dump(self, data, many, **kwargs):
        unpack = data["request"]
        unpack["provider"] = "BNI_RDL"
        return unpack


class BniOpgTransferSchema(Schema):
    """ schema used for transfer using BNI OPG """

    source = fields.Str(attribute="debitAccountNo")
    destination = fields.Str(attribute="creditAccountNo")
    currency = fields.Str(attribute="valueCurrency")
    amount = fields.Str(attribute="valueAmount")
    remark = fields.Str()
    reference = fields.Str(attribute="customerReferenceNumber")

    class Meta:
        unknown = EXCLUDE

    @post_dump
    def custom_dump(self, data, many, **kwargs):
        data["provider"] = "BNI_OPG"
        return data