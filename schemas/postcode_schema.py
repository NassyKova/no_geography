from main import ma
from marshmallow import fields

class PostcodeSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["postcode_id","postcode", "state"]
        # load_only = ["address_id"]
    # Schema is defined as a String, to avoid the circular import error

postcode_schema = PostcodeSchema()
postcodes_schema = PostcodeSchema(many=True)