from flask_restx import Api
from .users import user_api
from .groups import group_api
from .sessions import session_api

api = Api(
    title='Pantheon API',
    version='1.0',
    description='REST API Documentation for Pantheon.',
    # All API metadatas
)

api.add_namespace(user_api)
api.add_namespace(group_api)
api.add_namespace(session_api)