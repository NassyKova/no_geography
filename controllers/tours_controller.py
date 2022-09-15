from flask import Blueprint, jsonify
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
    #result = cards_schema.dump(cards_list)
    # return the data in JSON format
    #return jsonify(result)
    tours_list = Tour.query.all()
    result = tour_schema.dump(tours_list)
    return jsonify(result), #200