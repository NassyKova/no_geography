from main import db

class Card(db.Model):
    # define the table name for the db
    __tablename__ = "ADDRESSES"
        # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
address_id = db.Column(db.Integer, primary_key=True)
street_number = db.Column(db.Integer)
street_name = db.Column(db.String())
suburb = db.Column(db.String)
postcode_id = db.Column(db.Integer, foreign_keys=True)
