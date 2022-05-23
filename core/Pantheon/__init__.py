from flask_restx import Api
from core.Users.API import user_api
from core.Groups.API import group_api
from core.Sessions.API import session_api

from .AppFactory import *
from .Namespaces import *

api = Api(
    title='Pantheon API',
    version='1.0',
    description='REST API Documentation for Pantheon.',
    # All API metadatas
)

api.add_namespace(user_api)
api.add_namespace(group_api)
api.add_namespace(session_api)