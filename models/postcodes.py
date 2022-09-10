from main import db

class Card(db.Model):
    # define the table name for the db
    __tablename__ = "POSTCODES"
        # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
postcode_id = db.Column(db.Integer, primary_key=True)
postcode = db.Column(db.Integer, nullable=False)
state = db.Column(db.String(), nullable=False)
