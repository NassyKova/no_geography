from flask import Blueprint, jsonify, request
from main import db
from models.tours import Tour
from schemas.tour_schema import tour_schema, tours_schema

tours = Blueprint('tours', __name__, url_prefix="/tours")

# The GET routes endpoint
@tours.route("/", methods=["GET"])
def get_tours():
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
    result = tour_schema.dump(tour)
    return jsonify(result)


@tours.route("/add", methods=["POST"])
def add_tour():
    # # it is not enough with a token, the identity needs to be a admin
    # if get_jwt_identity() != "admin":
    #     return {"error": "You don't have the permission to do this"}, 403    
    tour_fields = tour_schema.load (request.json)
    tour = Tour(
        title = tour_fields["title"],
        description = tour_fields["description"],
        date = tour_fields["date"],
        length = tour_fields["length"],
        cost = tour_fields["cost"],
        capacity = tour_fields["capacity"],
        address = tour_fields["address"],
        provider_id = tour_fields["provider_id"]
    )

    db.session.add(tour)
    db.session.commit()
    return jsonify(tour_schema.dump(tour))


@tours.route("/<int:id>", methods=["PUT"])
def update_tour(id):
    #find the tour in the database
    tour = Tour.query.get(id)
        #get the tour details from the request
    tour_fields = tour_schema.load(request.json)
    #upodate the values of the tour
    tour.title = tour_fields["title"]
    tour.description = tour_fields["description"]
    tour.date = tour_fields["date"]
    tour.length = tour_fields["length"]
    tour.cost = tour_fields["cost"]
    tour.capacity = tour_fields["capacity"]
    tour.address = tour_fields["address"]
    tour.provider_id = tour_fields["provider_id"]

    #save changes in the database
    db.session.commit() 

    return jsonify(tour_schema.dump(tour)), 201  


