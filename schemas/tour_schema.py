from main import ma
from marshmallow import fields
from schemas.address_schema import AddressSchema
from schemas.provider_schema import ProviderSchema

class TourSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["title","description", "tour_id", "date", "length", "cost", "capacity", "address", "provider_id", "provider", "address"]
        load_only = ["provider_id", "address_id"]
    # Schema is defined as a String, to avoid the circular import error
    provider = fields.Nested("ProviderSchema", only=("name",))
    address = fields.Nested("AddressSchema", only=("street_number", "street_name", "suburb",))

    # address = fields.Nested(AddressSchema)

# single tour schema
tour_schema = TourSchema()
# multyply schema
tours_schema = TourSchema(many=True)
