from modules.Pantheon.Factory import ma
from marshmallow_sqlalchemy import fields


# this is what's ALLOWED TO BE presented to the user
# constrained by API MODEL
class NestedUser(ma.Schema):
    class Meta:
        fields = (
            "username",
            "uuid"
        )


# this is what's ALLOWED TO BE presented to the user
# constrained by API MODEL
class GroupSchema(ma.Schema):
    class Meta:
        fields = (
            "name",
            "guid",
            'creation_date',
            'members'
        )
    members = fields.Nested( NestedUser, many=True )


group_schema = GroupSchema()
groups_schema = GroupSchema( many=True )