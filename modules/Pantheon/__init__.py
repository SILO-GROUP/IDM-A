from flask_restx import Api
from modules.Users.API import api as user_api
from modules.Groups.API import api as group_api
from modules.Sessions.API import api as session_api
from modules.Emails.API import api as email_api
from modules.Pantheon.Config import system_config
from modules.Pantheon.Factory import app

authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    title=system_config.title,
    version=system_config.version,
    description=system_config.description,
    authorizations=authorizations,
    security='apiKey'
)

api.add_namespace(user_api)
api.add_namespace(group_api)
api.add_namespace(session_api)
