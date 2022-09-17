from main import ma
from marshmallow import fields

class ProviderSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["provider_id","name", "website", "bank_bsb", "bank_acc_number", "address_id"]
        load_only = ["address_id"]
    # Schema is defined as a String, to avoid the circular import error
    address = fields.Nested("AddressSchema", only=("suburb",))

provider_schema = ProviderSchema()
providers_schema = ProviderSchema(many=True)
