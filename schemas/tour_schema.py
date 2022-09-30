from main import ma
from marshmallow import fields
# from schemas.address_schema import AddressSchema
# from schemas.provider_schema import ProviderSchema
from schemas.postcode_schema import PostcodeSchema

class TourSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["title","description", "tour_id", "date", "time", "length", "cost", "capacity", "address_id", "postcode_id", "provider_id", "provider", "address", "postcode"]
        load_only = ["provider_id", "address_id"]
    title = ma.String(required = True)
    date = ma.DateTime(required = True)
    length = ma.String(required = True)
    description = ma.String(required = True)
    cost = ma.Integer(required = True)
    capacity = ma.Integer(required = True)

    # Schemas imported above
    provider = fields.Nested("ProviderSchema", only=("name",))
    address = fields.Nested("AddressSchema", only=("suburb", "postcode",))

# single tour schema
tour_schema = TourSchema()
# multyply schema
tours_schema = TourSchema(many=True)
