from main import ma
from marshmallow import fields
from schemas.address_schema import AddressSchema
from schemas.provider_schema import ProviderSchema
from schemas.postcode_schema import PostcodeSchema

class TourSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["title","description", "tour_id", "date", "length", "cost", "capacity", "address_id", "postcode_id", "provider_id", "provider", "address", "postcode"]
        load_only = ["provider_id", "address_id"]
    # Schema is defined as a String, to avoid the circular import error
    provider = fields.Nested("ProviderSchema", only=("name",))
    # address = fields.Nested("AddressSchema", only=("street_number", "street_name", "suburb",))
    address = fields.Nested("AddressSchema", only=("suburb", "postcode",))
    postcode = fields.Nested("PostcodeSchema", only=("postcode", "state",))

    # address = fields.Nested(AddressSchema)

# single tour schema
tour_schema = TourSchema()
# multyply schema
tours_schema = TourSchema(many=True)
