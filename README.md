# Anastasia Dyakova T2a

> ## R1	Identification of the problem you are trying to solve by building this particular app.
A friend of mine is running a travel group on MeetUp, they run it by themselves. We were discussing the possibilities of growing the business. One of the idea was about combinging different small tour groups similar to what my friend made together. Having all the groups in one place will be benefecial for the group owners - client base will be increasing 
### User story.
    Janice 26
    "My family and I are quite social and active. We like to go for a hike or rent a couple of kayaks and spend exploring a lake, or go for a walk in a forrest. It's nice to meet likeminded peope and make new friends. I want to have an easy access to the all the activities in my area and easily book something that I like"
> ## R2	Why is it a problem that needs solving?
At the moment if client wants to book different tours, they need to to be signed up in different groups. It leads to different websites, different logins and passwords. For the businees it means that they can loose the client with time.
Having one database for all the tours created by different groups is beneficial for everyone:
For the busines
- Shared clientbase, works for promo, targeting by location, activity tupe, etc
- Easy to be found by people who are already interested in the product

For the client
- One website, one login and password
- Easy search using postcodes
- potentially make a forum/social network, easier to meet with people


> ## R3	Why have you chosen this database system. What are the drawbacks compared to others?
For this project we use PostgreSQL database.
Postgres is a very well documented database system, it's open sourced and free. It works well with external databases and runs on different platforms. Nested databases transactions let the database be more adaptable. Creating and dropping the tables is very simple to use.

Drawback for postgres would be
Horisontal scaling can get complicated, requires additional solutions to make it easily useble.
Not the best solution for large scale applications, it might work noticably slow.
According to database structure, we can't have more fields than already had been defined in the database. To cxhange that, we need to go thought the code and implement the change in every place that has a connection.
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
Whule creating this app we added different third part cervice such as:
- psycopg2 is a popular database adapter for Python for creating connections in Flask
- SQLAlchemy lets connect Flaks and Postgresql:
- marshmallow lets serialized the data, converting complex database to and from Python daratypes
- marshmallow-sqlalchemy is an integreation marshmallow and SQLAlchemy
- Blueprints lets define some of the properties which it can be used at any time in the app
- flask-bcrypt provide bcrypt hashing - talking a pice of data of any size and coverting to a pice of dada with fixed size. Used for passwords and other sensitive data
- flask-jwt-extended lets create different types of tokens that used for validation and security purposes. It also allows to call a special identity for validation purposes

> ## R8	Describe your projects models in terms of the relationships they have with each other
1 provider can have many tours. 
1 provider has one address.
1 tour has 1 address
1 address has 1 postcode
1 booking has one tour
1 client can have many bookings
1 tour has 1 address
> ## R9	Discuss the database relations to be implemented in your application
In our application we wanyed to implement 
> ## R10	Describe the way tasks are allocated and tracked in your project
trello board