# Anastasia Dyakova T2a

> ## R1	Identification of the problem you are trying to solve by building this particular app.
A friend of mine is running a travel group on MeetUp, they run it by themselves. We were discussing the possibilities of growing the business. One of the idea was about combinging different small tour providing  groups similar to what my friend made. Having all the groups in one place will be benefecial for the group owners - client base will be increasing 
### User story.
    Janice 26
    "My family and I are quite social and active. We like to go for a hike or rent a couple of kayaks, walk in a forrest. It's nice to meet likeminded peope and make new friends. I want to have an easy access to the all the activities in my area and easily book something that I like. I aslo would like to see past events I attended"
> ## R2	Why is it a problem that needs solving?

> ## R3	Why have you chosen this database system. What are the drawbacks compared to others?
For this project we use PostgreSQL database.
Postgres is a very well documented database system, it's open sourced and free. It works well with external databases and runs on different platforms. Nested databases transactions let the database be more adaptable. Creating and dropping the tables is very simpl to use.

Drawback for postgres would be
Horisontal scaling can get complicated, requires additional solutions to make it easily useble.
Not the best solution for large scale applications, it might work noticably slow.
According to database structure, we can't have nore fields than already had been defined in the database. To cxhange that, we need to go thought the code and implement the change in every place that has a connection.
Opensource also comes with no warranty and no liability


> ## R4	Identify and discuss the key functionalities and benefits of an ORM
Object-relational mapping connects the code and the database.
> ## R5	Document all endpoints for your API
### Authoisational routes
- __@auth.route("/register", methods=["POST"])__ register new clients
- __@auth.route("/login", methods=["POST"])__ log in existing clients
- __@auth.route("/admin/login", methods=["POST"])__ admin login, jwt requred
### Tours routes
- __@tours.route("/", methods=["GET"])__ get all the tours
- __@tours.route("/<int:id>", methods=["GET"])__ get information about tour by tour id
- __@tours.route("/postcode/<int:postcode>", methods=["GET"])__ find tours by postcode
- __@tours.route("/add", methods=["POST"])__ add new tour, by admin only, jwt required
- __@tours.route("/<int:id>", methods=["PUT"])__ update excisting tour, by admin only, jwt required
### Providers routes
- __@providers.route('/', methods=['GET'])__ get all the providers, by admin only
- __@providers.route("/<int:id>", methods=['GET'])__ shows 1 provider choosen by id, admin only
- __@providers.route("/add", methods=["POST"])__ adding new provider, admin only
### Bookings routes
- __@bookings.route('/', methods=["GET"])__ get all the bookings, admin only
- __@bookings.route("<int:tour_id>/add/<int:client_id>", methods=["POST"])__ add new booking using tour id and client id, admin only

> ## R6	An ERD for your app
![]()
> ## R7	Detail any third party services that your app will use
- psycopg2 To create the connection in Flask we need Psycopg, which is the most popular PostgreSQL database adapter for Pytho
- SQLAlchemy SQLAlchemy is the ORM we will use to connect Flask and PostgreSQL, so let's install that as well:
- marshmallow. This means that the data we get from a database is not serialized, it is not considered a list. To do that we can get help of a package like marshmallow
- blueprintsBlueprints are basically a way of defining some of the properties of a Flask app in advance, so that you can pick when that definition takes effect, and even apply your defined behaviour to multiple apps if you want. 
- flask-bcrypt To keep the users password safe in our database we will use hashing. The technical definition of a hash function is the ability for the function to take a piece of data of any size and create a piece of data from the original in a fixed size.An example would be if we take a piece of text and hash it with a hasing function such as sha256. We are returned a piece of data with a fixed length of 256 bits. For our server we'll use a slow-hashing library like flask-bcrypt. I
from marshmallow import ValidationError
from marshmallow.validate import Length
- flask-jwt-extended

> ## R8	Describe your projects models in terms of the relationships they have with each other
1 provider can have many tours. 
1 provider has one address.
1 tour has 1 address
1 addrees has 1 postcodes
1 booking has one tour
1 client can have many bookings
1 tour has 1 address
> ## R9	Discuss the database relations to be implemented in your application
erd vs models
> ## R10	Describe the way tasks are allocated and tracked in your project
trello board