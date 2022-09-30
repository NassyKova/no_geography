from urllib import response
from flask import Blueprint, jsonify, request
from main import db
from models.tours import Tour
from schemas.tour_schema import tour_schema, tours_schema
from schemas.address_schema import address_schema
from schemas.postcode_schema import postcode_schema
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from sqlalchemy import text
import json
from sqlalchemy.sql import select
from sqlalchemy import and_, or_


tours = Blueprint('tours', __name__, url_prefix="/tours")

# The GET routes endpoint
@tours.route("/", methods=["GET"])
def get_tours():
    # show the contnet of the query string
    print(request.query_string)
    # get all the tours from the db
    tours_list = Tour.query.all()
    # Convert the tours from the database into a JSON format and store them in result
    result = tours_schema.dump(tours_list)
    # # return the data in JSON format
    return jsonify(result)

    # tours_list = Tour.query.all()
    # result = tours_schema.dump(tours_list)
    # return jsonify(result), #200


@tours.route("/<int:id>", methods=["GET"])
def get_tour(id):
    # get the tour from the database by id
    tour = Tour.query.get(id)
    if not tour:
        return {"error": "no such tour id"}, 404
    result = tour_schema.dump(tour)
    return jsonify(result)


@tours.route("/postcode/<int:postcode>", methods=["GET"])
def get_tour_postcode(postcode):
    # RAW sql command to filter tours by postcode
    tour = text('''SELECT tours.title, suburb, postcode
    FROM tours, addresses, postcodes
    WHERE tours.address_id = addresses.address_id 
    AND addresses.postcode_id = postcodes.postcode_id
    AND postcode = :e1''')
    # get the tours filtered by postcode
    result = db.engine.execute(tour, {"e1":postcode})
    variable = json.dumps([dict(r) for r in result])
    if variable == "[]":
        return {"error": "no tours in this area"}, 404
    return variable



@tours.route("/add", methods=["POST"])
@jwt_required()
def add_tour():
        #the identity needs to be an admin
    if get_jwt_identity() != "admin":
        return {"error": "You don't have the permission to do this"}, 403    
    tour_fields = tour_schema.load (request.json)
    tour = Tour(
        title = tour_fields["title"],
        description = tour_fields["description"],
        date = tour_fields["date"],
        time = tour_fields["time"],
        length = tour_fields["length"],
        cost = tour_fields["cost"],
        capacity = tour_fields["capacity"],
        address_id = tour_fields["address_id"],
        provider_id = tour_fields["provider_id"]
    )

    db.session.add(tour)
    db.session.commit()

    return jsonify(tour_schema.dump(tour)), 201 


@tours.route("/<int:id>", methods=["PUT"])
@jwt_required()
def update_tour(id):
        #the identity needs to be an admin
    if get_jwt_identity() != "admin":
        return {"error": "You don't have the permission to do this"}, 403 
    #find the tour in the database
    tour = Tour.query.get(id)
    if not tour:
        return {"error": "no such tour id"}, 404
    #get the tour details from the request
    tour_fields = tour_schema.load(request.json)
    #upodate the values of the tour
    tour.title = tour_fields["title"]
    tour.description = tour_fields["description"]
    tour.date = tour_fields["date"]
    tour.length = tour_fields["length"]
    tour.cost = tour_fields["cost"]
    tour.capacity = tour_fields["capacity"]
    tour.address_id = tour_fields["address_id"]
    tour.provider_id = tour_fields["provider_id"]
    #save changes in the database
    db.session.commit() 
    return jsonify(tour_schema.dump(tour)), 201  



@tours.errorhandler(ValidationError)
def register_validation_error(error):
    #print(error.messages)
    return error.messages, 400


