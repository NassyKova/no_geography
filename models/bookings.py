from main import db

class Booking(db.Model):
    __tablename__ = "bookings"

    booking_id = db.Column(db.Integer, primary_key=True)
    # tour_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    # client_id = db.Column(db.Integer, foreign_key=True, nullable=False)
    tour_id = db.Column(db.Integer, db.ForeignKey("tours.tour_id"), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey("clients.client_id"), nullable=False)