from main import ma
from marshmallow import fields
from marshmallow.validate import Length

class ClientSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["client_id","email", "password", "phone", "f_name", "l_name"]
    #add validation to password
    password = ma.String(validate=Length(min=8))
        # load_only = ["provider_id"]
    # Schema is defined as a String, to avoid the circular import error
    # provider = fields.Nested("ProviderSchema", only=("name",))

# single client schema
client_schema = ClientSchema()
# multiply schema
clients_schema = ClientSchema(many=True)

