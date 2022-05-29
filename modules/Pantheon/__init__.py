from flask_restx import Api
from modules.Users.API import api as user_api
from modules.Groups.API import group_api
from modules.Sessions.API import session_api

from .Factory import app

authorizations = {
    'apiKey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    title='Pantheon API',
    version='1.0',
    description='REST API Documentation for Pantheon.',
    authorizations=authorizations,
    security='apiKey'
)

api.add_namespace(user_api)
api.add_namespace(group_api)
api.add_namespace(session_api)
