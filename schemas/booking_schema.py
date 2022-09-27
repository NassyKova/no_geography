from main import ma
from marshmallow import fields
# from schemas.client_schema import ClientSchema
#from schemas.tour_schema import TourSchema

class BookingSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("booking_id", "client_id", "tour_id", "client", "tour")
        # If not ID's required:
        # load_only = ("client_id", "tour_id")
    # what shows after booking added
    client = fields.Nested("ClientSchema", only=("f_name", "l_name"))
    tour = fields.Nested("TourSchema", only=("title",))
booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)


