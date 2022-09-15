from main import ma
from marshmallow import fields

class TourSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["tour_id", "title", "description", "dates", "length", "cost", "capacity", "status", "addresses", "provider_id"]
        load_only = ["provider_id"]
    # Schema is defined as a String, to avoid the circular import error
    # provider = fields.Nested("ProviderSchema", only=("name",))

# single tour schema
tour_schema = TourSchema()
# multyply schema
tours_schema = TourSchema(many=True)
