from main import db

class Card(db.Model):
    # define the table name for the db
    __tablename__ = "TOURS"
        # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
tour_id = db.Column(db.Integer, primary_key=True)
title = db.Column(db.String(), nullable=False)
desciprion = db.Column(db.String())
dates = db.Column(db.DateTime)
length = db.Column(db.Integer)
cost = db.Column(db.Integer)
capacity = db.Column(db.Integer)
status = db.Column(db.Boolean, default=True)
addresses = db.Column(db.Integer, foreign_keys=True)
provider_id = db.Column(db.Integer, foreign_keys=True)