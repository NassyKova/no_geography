from main import db
from datetime import date

class Booking(db.Model):
    __tablename__ = "bookings"

    booking_id = db.Column(db.Integer, primary_key=True)
    tour_id = db.Column(db.Integer, db.ForeignKey("tours.tour_id"), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.client_id"), nullable=False)
    created = db.Column(db.DateTime, default=date.today())