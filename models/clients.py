from main import db

class Card(db.Model):
    # define the table name for the db
    __tablename__ = "CLIENTS"
        # Set the primary key, we need to define that each attribute is also a column in the db table, remember "db" is the object we created in the previous step.
client_id = db.Column(db.Integer, primary_key=True)
email = db.Column(db.String(), nullable=False)
password = db.Column(db.String(), nullable=False)
phone = db.Column(db.Integer)
f_name = db.Column(db.String())
l_name = db.Column(db.String(), nullable=False)
