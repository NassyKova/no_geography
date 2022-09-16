from flask import Blueprint, jsonify, request
from main import db
from models.tours import Tour
from models.bookings import Booking
from models.clients import Client
from schemas.tour_schema import tour_schema, tours_schema
from schemas.booking_schema import booking_schema, bookings_schema
from flask_jwt_extended import jwt_required, get_jwt_identity

bookings = Blueprint('bookings', __name__, url_prefix="/bookings")

# get all bookings
# RIGHT NOW JUST ID
@bookings.route('/', methods=["GET"])
def get_all_bookings():
    bookings_list = Booking.query.all()
    result = bookings_schema.dump(bookings_list)
    return jsonify(result)

# # post a new booking
# @bookings.route("<int:tour_id>/new", methods=["POST"])
# @jwt_required()
# def new_reservation(tour_id):
# #     #find the tourin the database
#     tour = Tour.query.get(tour_id)
# #     #check if book exist in the database
# #     if not book:
# #         return {"error": "Book id not found in the database"}, 404
#     client_id = get_jwt_identity()
#     client = Client.query.get(client_id)
#     if not client:
#         return {"error": "User not found in the database"}, 404

#     booking = Booking(
#         client = client,
#         tour = tour,
#     )

#     db.session.add(booking)
#     db.session.commit()

#     return jsonify(booking_schema.dump(booking))