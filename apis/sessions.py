from flask_restx import Resource
from flask import request

from apis.APIModels.User import UserFields, UserCreateFields, UserUpdateFields
from apis.namespaces import session_api
from core.logic.Users import UserController

@session_api.route('/all')
class Users(Resource):
    @session_api.doc('list_users')
    @session_api.marshal_list_with(UserFields)
    def get(self):
        '''List all users.'''
        users = ucon.get_all()
        if users is None:
            return 'No users found.', 404

        return users
