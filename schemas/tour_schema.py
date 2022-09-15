from main import ma
from marshmallow import fields

class TourSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["title","description", "tour_id", "date", "length", "cost", "capacity", "address", "provider_id"]
        load_only = ["provider_id"]
    # Schema is defined as a String, to avoid the circular import error
    provider = fields.Nested("ProviderSchema", only=("name",))

# single tour schema
tour_schema = TourSchema()
# multyply schema
tours_schema = TourSchema(many=True)
