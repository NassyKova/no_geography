from flask import Blueprint, jsonify, request
from main import db
from schemas.provider_schema import provider_schema, providers_schema
from models.providers import Provider
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError

providers = Blueprint('providers', __name__, url_prefix="/providers")

@providers.route('/', methods=['GET'], strict_slashes=False)
@jwt_required()
def get_providers():
    if get_jwt_identity() != "admin":
        return {"error": "You don't have the permission to do this"}, 403  
        # get all the providersfrom the db
    providers_list = Provider.query.all()
        # Convert the providers from the database into a JSON format and store them in result
    result = providers_schema.dump(providers_list)
    # # return the data in JSON format
    return jsonify(result)


@providers.route("/<int:id>", methods=['GET'])
@jwt_required()
def get_provider(id):
    if get_jwt_identity() != "admin":
        return {"error": "You don't have the permission to do this"}, 403  
        # get the provider from the db
    provider = Provider.query.get(id)
    if not provider:
        return {"error": "no such provider id"}, 404
        # Convert the provider from the database into a JSON format and store it in result
    result = provider_schema.dump(provider)
    # # return the data in JSON format
    return jsonify(result)

# add new provider
@providers.route("/add", methods=["POST"])
@jwt_required()
def add_provider():
        #the identity needs to be an admin
    if get_jwt_identity() != "admin":
        return {"error": "You don't have the permission to do this"}, 403    
    provider_fields = provider_schema.load (request.json)
    # check the client by phone to check if is'a already in the db
    provider = Provider.query.filter_by(name=provider_fields["name"]).first()
    if provider:
        return {"error": "This provider has already been registered"}, 400
    provider = Provider(
        name = provider_fields["name"],
        website = provider_fields["website"],
        bank_bsb = provider_fields["bank_bsb"],
        bank_acc_number = provider_fields["bank_acc_number"],
        address_id = provider_fields["address_id"]
    )

    db.session.add(provider)
    db.session.commit()
    return jsonify(provider_schema.dump(provider)), 201

@providers.errorhandler(ValidationError)
def register_validation_error(error):
    #print(error.messages)
    return error.messages, 400
