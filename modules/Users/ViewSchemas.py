from modules.Pantheon.Factory import ma
from marshmallow_sqlalchemy import fields


# for representation of groups associated with the user
class NestedGroup(ma.Schema):
    class Meta:
        fields = (
            "name",
            "uuid",
        )


# for representation of a user
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