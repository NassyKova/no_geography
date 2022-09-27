from main import ma
from marshmallow import fields
from schemas.address_schema import AddressSchema

class ProviderSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["provider_id","name", "website", "bank_bsb", "bank_acc_number", "address_id"]
        load_only = ["address_id"]
    name = ma.String(required = True)
    website = ma.String(required = True)
    bank_bsb = ma.Integer(required = True)
    bank_acc_number = ma.Integer(required = True)
    address_id = ma.Integer(required = True)

    # Schema is defined as a String, to avoid the circular import error
    # shows suburb only in the tour information
    address = fields.Nested("AddressSchema", only=("suburb",))

provider_schema = ProviderSchema()
providers_schema = ProviderSchema(many=True)
