from main import ma
from marshmallow.validate import Length

class AdminSchema(ma.Schema):
    class Meta:
        fields = ('admin_id', "email", "password", "name")

    email = ma.Field(required = True)
    password = ma.String(validate=Length(min=8), required=True)


#just the single schema for log in purposes
admin_schema = AdminSchema()