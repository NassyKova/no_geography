from datetime import timedelta
from flask import Blueprint, jsonify, request
from models.clients import Client
from models.admin import Admin
from schemas.client_schema import client_schema
from schemas.admin_schema import admin_schema
from main import db, bcrypt, jwt
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError


auth = Blueprint('auth', __name__, url_prefix="/auth")


@auth.route("/register", methods=["POST"])
def register_client():
    # get the client's details from the request
    client_fields = client_schema.load(request.json)
    # check the client by email to check if is'a already in the db
    client = Client.query.filter_by(email=client_fields["email"]).first()
    if client:
        return {"error": "This email has already been registered"}

    # check the client by phone to check if is'a already in the db
    client = Client.query.filter_by(phone=client_fields["phone"]).first()
    if client:
        return {"error": "This phone has already been registered"}

    #create client Object
    client = Client(
        email = client_fields["email"],
        password = bcrypt.generate_password_hash(client_fields["password"]).decode("utf-8"),
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


# client's login
@auth.route("/login", methods=["POST"])
def login_client():
    # get the client's details from the request
    client_fields = client_schema.load(request.json)
    # Check email and password. Client needs to exist, and password needs to match    
    client = Client.query.filter_by(email=client_fields["email"]).first()
    if not client:
        return {"error": "email is not found"}
    if not bcrypt.check_password_hash(client.password, client_fields["password"]):
        return {"error": "wrong password"}
    # Credentials are valid, so generate token and return it to the client
    token = create_access_token(identity=str(client.client_id), expires_delta=timedelta(days=1))
    return {"email": client.email, "token": token}


# admin's login
@auth.route("/admin/login", methods=["POST"])
def login_admin():
        # get email and password from the request
    admin_fields = admin_schema.load(request.json)
    # Check email and password. Adminneeds to exist, and password needs to match 
    admin = Admin.query.filter_by(email=admin_fields["email"]).first()
    if not admin:
        return {'error': "this email does not have asmin rights"}

    if not bcrypt.check_password_hash(admin.password, admin_fields["password"]):
        return {'error': "this password is not correct"}
    # Credentials are valid, so generate token and return it to the user
    token = create_access_token(identity="admin", expires_delta=timedelta(days=1))

    return {"email": admin.email, "token": token}

#example??
@auth.errorhandler(ValidationError)
def register_validation_error(error):
    #print(error.messages)
    return error.messages, 400