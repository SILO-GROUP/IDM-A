from modules.Pantheon.Factory import ma
from modules.Sessions.DatabaseModels import SessionModel
from modules.Users.DatabaseModels import UserModel
from modules.Groups.DatabaseModels import GroupModel
from marshmallow_sqlalchemy import fields


# this is what's ALLOWED TO BE presented to the user
# constrained by API MODEL
class NestedGroups(ma.Schema):
    class Meta:
        model = GroupModel
        fields = (
            "name",
            "uuid",
        )


# this is what's ALLOWED TO BE presented to the user
# constrained by API MODEL
class NestedUser(ma.Schema):
    class Meta:
        model = UserModel
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
        model = SessionModel
        fields = (
            "name",
            "uuid",
            'creation_date',
            'user'
        )
    user = fields.Nested( NestedUser, many=False )


session_schema = SessionSchema()
sessions_schema = SessionSchema( many=True )