from main import ma
from marshmallow import fields

class AddressSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["address_id","street_number", "street_name", "suburb", "postcode_id", "postcode"]
        load_only = ["postcode_id"]
    # Schema is defined as a String, to avoid the circular import error
    postcode = fields.Nested("PostcodeSchema", only=("postcode", "state",))

address_schema = AddressSchema()
addresses_bookings_schema = AddressSchema(many=True)
