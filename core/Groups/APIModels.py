# API Models: GROUPS
# These APIModels tell swagger what values to expect.

from flask_restx import fields
from core.Pantheon.Namespaces import group_api


# OUTPUT fields for showing to the group
# @api.marshal_with
MemberFields = group_api.model(
    'secure_user_view', {
        'uuid': fields.String( required=False, description='Identifier of the User.'),
        'username': fields.String( required=True, description='The username of the user.')
    }
)

GroupFields = group_api.model(
    'secure_group_view', {
        'uuid': fields.String( required=False, description='Identifier of the group.'),
        'name': fields.String( required=True, description='The name of the group.'),
        'creation_date': fields.String( required=True, description='The creation time for the group.'),
        'members': fields.List( fields.Nested( MemberFields, many=True, exclude='groups') )
    }
)

# INPUT used for creation of group
# @api.expect()
GroupCreateFields = group_api.model(
    'create_group', {
        'name': fields.String( required=True, description='Username to create.' )
    }
)

GroupUpdateFields = group_api.model(
    'update_user', {
        'name': fields.String( required=True, description='New group name.' )
    }
)

GroupMemberModifyFields = group_api.model(
    'modify_group_members',
    {
        'uuid': fields.String( required=True, description="User UUID to modify this group with." )
    }
)