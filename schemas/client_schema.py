from main import ma
from marshmallow import fields
from marshmallow.validate import Length

class ClientSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["client_id","email", "password", "phone", "f_name", "l_name"]
    #add validation to password
    email = ma.String(required = True)
    password = ma.String(validate=Length(min=8), required=True)

        # load_only = ["provider_id"]
    # Schema is defined as a String, to avoid the circular import error
    # provider = fields.Nested("ProviderSchema", only=("name",))

# single client schema
client_schema = ClientSchema()
# multiply schema
clients_schema = ClientSchema(many=True)

