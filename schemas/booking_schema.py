from main import ma
from marshmallow import fields
# from schemas.client_schema import ClientSchema
from schemas.tour_schema import TourSchema

class BookingSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ("booking_id", "client_id", "tour_id")
        load_only = ("client_id", "tour_id")
booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)