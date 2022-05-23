from core.Pantheon import ma
from marshmallow_sqlalchemy import fields


# this is what's ALLOWED TO BE presented to the user
# constrained by API MODEL
class NestedGroups(ma.Schema):
    class Meta:
        fields = (
            "name",
            "uuid",
        )


# this is what's ALLOWED TO BE presented to the user
# constrained by API MODEL
class NestedUser(ma.Schema):
    class Meta:
        fields = (
            "username",
            "uuid",
            "groups"
        )
    groups = fields.Nested( NestedGroups, many=True )


# this is what's ALLOWED TO BE presented to the user
# constrained by API MODEL
class SessionSchema(ma.Schema):
    class Meta:
        fields = (
            "name",
            "uuid",
            'creation_date',
            'user'
        )
    user = fields.Nested( NestedUser, many=True )


session_schema = SessionSchema()
sessions_schema = SessionSchema( many=True )