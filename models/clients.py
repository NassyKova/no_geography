
from main import db

class Client(db.Model):
    # define the table name for the db
    __tablename__ = "clients"
        # Set the primary key, we need to define that each attribute is also a column in the db table
    client_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    phone = db.Column(db.Integer)
    f_name = db.Column(db.String())
    l_name = db.Column(db.String(), nullable=False)
    bookings = db.relationship(
        "Booking",
        backref="client",
        cascade="all, delete"
    )