"""
    Handle Serialization from BNI RDL And OPG
"""
from marshmallow import Schema, fields, EXCLUDE, post_dump


"""
    BNI RDL
"""


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
        return unpack


"""
    BNI OPG
"""


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


"""
    OY
"""


class OyDisburseSchema(Schema):
    """ schema used for transfer using BNI OPG """

    destination = fields.Str(attribute="recipient_account")
    bank_code = fields.Str(attribute="recipient_bank")
    amount = fields.Str()
    partner_trx_id = fields.Str()

    class Meta:
        unknown = EXCLUDE


class OyStaticVaSchema(Schema):
    """ schema used for transfer using BNI OPG """

    partner_user_id = fields.Str()
    bank_code = fields.Str()
    amount = fields.Decimal()
    is_open = fields.Boolean()
    is_single_use = fields.Boolean()
    is_lifetime = fields.Boolean()
    expiration_time = fields.Str()
    username_display = fields.Str()

    class Meta:
        unknown = EXCLUDE


class OyUpdateStaticVaSchema(Schema):
    """ schema used for transfer using BNI OPG """

    amount = fields.Decimal()
    is_open = fields.Boolean()
    is_single_use = fields.Boolean()
    is_lifetime = fields.Boolean()
    expiration_time = fields.Str()

    class Meta:
        unknown = EXCLUDE
