from main import db

class Provider(db.Model):
    # define the table name for the db
    __tablename__ = "providers"
        # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
    provider_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    website = db.Column(db.String())
    bank_bsb = db.Column(db.Integer)
    bank_acc_number = db.Column(db.Integer)
    address = db.Column(db.Integer, db.ForeignKey("addresses.address_id"), nullable=False)
