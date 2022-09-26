from flask import Blueprint
from main import db, bcrypt
from models.tours import Tour
from models.clients import Client
from models.providers import Provider
from models.bookings import Booking
from models.addresses import Address
from models.postcodes import Postcode
from models.admin import Admin
from datetime import date, time


db_commands = Blueprint("db", __name__)


@db_commands.cli.command('create')
def create_db():
    # Tell SQLAlchemy to create all tables for all models in the physical DB
    db.create_all()
    print('Tables created')


@db_commands.cli.command('drop')
def drop_db():
    # Tell SQLAlchemy to drop all tables
    db.drop_all()
    print('Tables dropped')


@db_commands.cli.command('seed')
def seed_db():

# admin seed
    admin1 = Admin(
        name = "Sarah the admin",
        email = "admin@email.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf8"),
    )
    db.session.add(admin1)

# clients seed
    client1 = Client(
        f_name = "Laura",
        l_name = "Scott",
        email = "client1@email.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf8"),
        phone = "0404000111"
    )
    db.session.add(client1)


    client2 = Client(
        f_name = "Max",
        l_name = "Orange",
        email = "client2@email.com",
        password = bcrypt.generate_password_hash("12345678").decode("utf8"),
        phone = "0404000222"
    )
    db.session.add(client2)

# posdcode seed
    postcode1 = Postcode(
        postcode = "3333",
        state = "VIC",
    )
    db.session.add(postcode1)

    postcode2 = Postcode(
        postcode = "3555",
        state = "VIC",
    )
    db.session.add(postcode2)
    # commit postcodes
    db.session.commit()

# addresses seeed
    address1 = Address(
        street_number = "11",
        street_name = "Blue rd",
        suburb = "Rosemary",
        postcode_id = postcode1.postcode_id,
    )
    db.session.add(address1)

    address2 = Address(
        street_number = "22",
        street_name = "Red rd",
        suburb = "Hot Springs",
        postcode_id = postcode1.postcode_id,
    )
    db.session.add(address2)
# commit addresses
    db.session.commit()


# providers seed
    provider1 = Provider(
        name = "No Geography",
        website = "nogeography.com",
        bank_bsb = "123456",
        bank_acc_number = "123456789",
        address_id = address1.address_id
    )
    db.session.add(provider1)

    provider2 = Provider(
        name = "Kayak Int",
        website = "kayakint.com",
        bank_bsb = "233456",
        bank_acc_number = "23456789",
        address_id = address2.address_id
    )
    db.session.add(provider2)
    db.session.commit()


# tours seed
    tour1 = Tour(
        title = "Cherry Lake",
        description = "Catch a train to Altona railway station on the Laverton line. Walk up Pier St, away from the main shopping centre area, \
        towards Altona Civic Centre on the corner of Millers Rd. Cross Millers Rd and walk in between the civic centre and Altona Bowling Club to Bluegum Drive.\
        Turn right, then left into Fresno St on the corner of J.K. Grant Reserve. Cherry Lake is now in front of you. \
        Your choice to walk either way all the way around.",
        date = date(day = 11, month = 6, year = 2023),
        time = time(hour=16, minute=20),
        length = "2 h",
        cost = "25",
        capacity = "10",
        address_id = address2.address_id,
        # add the id explicitly
        provider_id = provider1.provider_id
    )
    db.session.add(tour1)

    tour2 = Tour(
        title = "Stunning KingLake & Lake Nagambie",
        description = "Two days trip to Stunning KingLake & Lake Nagambie : Hiking + Kayaking & much more!\
        Let's 🎄surround ourselves with nature, waterfalls, forests, lakes, rivers 🏔 and great people vibes.\
        +Group dinner in Italian Winery\
        +Breakfast in a Unique local produce cafe\
        +Social drinks&Music night",
        date = date(day = 28, month = 2, year = 2022),
        time = time(hour = 16),
        length = "2 days",
        cost = "100",
        capacity = "10",
        address_id = address1.address_id,
        # add the object, SQLAlchemy will handle it 
        provider = provider2
    )
    db.session.add(tour2)
    # commit tours
    db.session.commit()


# bookings seed
    booking1 = Booking(
        tour_id = tour1.tour_id,
        client_id = client1.client_id
    )
    db.session.add(booking1)
    db.session.commit()

    booking2 = Booking(
        tour_id = tour2.tour_id,
        client_id = client2.client_id
    )
    db.session.add(booking2)
    db.session.commit()


    print("tables seeded")