# API Models: USERS
# These APIModels tell swagger what values to expect.

from flask_restx import fields
from modules.Pantheon.Namespaces import user_api


# OUTPUT fields for showing to the user
# @api.marshal_with
USessionFields = user_api.model(
    'embedded_session_view', {
        'uuid': fields.String( required=True, description='UUID of the session.' ),
        'creation_date': fields.String( required=True, description='The creation time for the session.')
    }
)


UGroupFields = user_api.model(
    'secure_group_view', {
        'uuid': fields.String( required=False, description='Identifier of the group.'),
        'name': fields.String( required=True, description='The name of the group.')
    }
)

UserFields = user_api.model(
    'secure_user_view', {
        'uuid': fields.String( required=False, description='Identifier of the User.'),
        'username': fields.String( required=True, description='The username of the user.'),
        'creation_date': fields.String( required=True, description='The creation time for the user.'),
        'active': fields.Boolean( required=True, description='Is the account active?'),
        'email_verified': fields.Boolean( required=True, description='Has the email been verified?' ),
        'identity_verified': fields.Boolean( required=True, description="Has the user's identity been verified?"),
        'groups': fields.List( fields.Nested( UGroupFields, many=True )),
        'sessions': fields.List( fields.Nested( USessionFields, many=True )),
    }
)

# INPUT used for creation of users
# @api.expect()
UserCreateFields = user_api.model(
    'create_user', {
        'username': fields.String( required=True, description='Username to create.' ),
        'email': fields.String( required=True, description='Email address of the user being created.' ),
        'password': fields.String( required=True, description='Password of the user being created.' )
    }
)

UserUpdateFields = user_api.model(
    'update_user', {
        'username': fields.String( required=True, description='Username to create.' ),
        'email': fields.String( required=True, description='Email address of the user being created.' ),
        'password': fields.String( required=True, description='Password of the user being created.' )
    }
)

