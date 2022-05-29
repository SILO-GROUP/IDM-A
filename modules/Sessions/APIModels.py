# API Models: SESSIONS
# These APIModels tell swagger what values to expect.

from flask_restx import fields
from modules.Pantheon.Namespaces import session_api

SessionCreateFields = session_api.model(
    'create_session',
    {
        'uuid': fields.String( required=True, description="The user UUID to log in as." ),
        'password': fields.String( required=True, description="The password of the user trying to log in.")
    }
)

SessionFields = session_api.model(
    'secure_session_view',
    {
        'suid': fields.String(required=True, description="The session SUID."),
        'creation_date': fields.String(required=True, description="Creation time of the session.")
    }
)

UGroupFields = session_api.model(
    'secure_group_view_session', {
        'guid': fields.String( required=False, description='Identifier of the group.'),
        'name': fields.String( required=True, description='The name of the group.')
    }
)


# OUTPUT fields for showing to the group
# @api.marshal_with
SessionEmbeddedUser = session_api.model(
    'secure_user_view_session', {
        'uuid': fields.String( required=False, description='Identifier of the User.'),
        'username': fields.String( required=True, description='The username of the user.'),
        'groups': fields.List( fields.Nested( UGroupFields, many=True ))
    }
)


InsecureSessionFields = session_api.model(
    'insecure_session_view',
    {
        'suid': fields.String( required=True, description="The session SUID."),
        'creation_date': fields.String(required=True, description="Creation time of the session."),
        'user': fields.Nested( SessionEmbeddedUser, many=False)
    }
)
