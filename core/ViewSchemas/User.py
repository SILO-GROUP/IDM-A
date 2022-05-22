from core.Pantheon.AppFactory import ma
from marshmallow_sqlalchemy import fields
from core.ViewSchemas.Group import GroupSchema
from core.DatabaseModels.User import UserModel


class NestedGroup(ma.Schema):
    class Meta:
        fields = (
            "name",
            "uuid",
            'creation_date'
        )



# this is what's ALLOWED TO BE presented to the user
# constrained by API MODEL
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "username",
            "uuid",
            'creation_date',
            'email_verified',
            'identity_verified',
            'creation_date',
            'active',
            'groups'
        )
    groups = fields.Nested( NestedGroup, many=True )


user_schema = UserSchema()
users_schema = UserSchema(many=True)