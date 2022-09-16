from datetime import timedelta
from flask import Blueprint, jsonify, request
from models.clients import Client
from schemas.client_schema import client_schema
from main import db, jwt, bcrypt
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth = Blueprint('auth', __name__, url_prefix="/auth")

@auth.route("/register", methods=["POST"])
def register_client():
    # get the client's details from the request
    client_fields = client_schema.load(request.json)
    # check the client by email to check if is'a already in the db
    client = Client.query.filter_by(email=client_fields["email"]).first
    if client:
        return {"error": "This email has already been registered"}

    # check the client by phone to check if is'a already in the db
    client = Client.query.filter_by(phone=client_fields["phone"]).first
    if client:
        return {"error": "This phone has already been registered"}

    #create client Object
    client = Client(
        email = client_fields["email"],
        password = bcrypt.generate_password_hash(client["password"]).decode("utf-8"),
        phone = client_fields["phone"],
        f_name = client_fields["f_name"],
        l_name = client_fields["l_name"],
    )

    # add the client to db
    db.session.add(client)
    # save the changes in the db
    db.session.commit()

    # generate the token setting the identity (client_id) and expiry time (1 day)
    token = create_access_token(identity=str(client.client_id),expires_delta=timedelta(days=1))

    return {"email": client.email, "token": token, "f_name": client.f_name, "l_name": client.l_name, "phone": client.phone}