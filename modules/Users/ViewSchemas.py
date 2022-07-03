from modules.Pantheon.Factory import ma
from marshmallow_sqlalchemy import fields


# for representation of groups associated with the user
class NestedGroup(ma.Schema):
    class Meta:
        fields = (
            "name",
            "guid",
        )


class NestedSession(ma.Schema):
    class Meta:
        fields = (
            'suid',
            'creation_date'
        )


# for representation of a user
class UserSchema(ma.Schema):
    class Meta:
        fields = (
            "username",
            "uuid",
            "email",
            'creation_date',
            'email_verified',
            'identity_verified',
            'creation_date',
            'active',
            'groups',
            'sessions',
        )
    groups = fields.Nested( NestedGroup, many=True )
    sessions = fields.Nested( NestedSession, many=True )


user_schema = UserSchema()
users_schema = UserSchema(many=True)