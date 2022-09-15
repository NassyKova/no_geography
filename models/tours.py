from main import db

class Tour(db.Model):
    # define the table name for the db
    __tablename__ = "tours"
        # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    tour_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String())
    dates = db.Column(db.DateTime)
    length = db.Column(db.String)
    cost = db.Column(db.Integer)
    capacity = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=True)
    address = db.Column(db.Integer, db.ForeignKey("addresses.address_id"), nullable=False)
    provider_id = db.Column(db.Integer, db.ForeignKey("providers.provider_id"), nullable=False)