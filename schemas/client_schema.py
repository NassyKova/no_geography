from main import ma
from marshmallow import fields

class ClientSchema(ma.Schema):
    class Meta:
        ordered = True
        fields = ["client_id","email", "password", "phone", "f_name", "l_name"]
        # load_only = ["provider_id"]
    # Schema is defined as a String, to avoid the circular import error
    # provider = fields.Nested("ProviderSchema", only=("name",))

# single client schema
client_schema = ClientSchema()
# multyply schema
clients_schema = ClientSchema(many=True)

