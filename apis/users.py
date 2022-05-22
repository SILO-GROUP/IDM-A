from flask_restx import Resource
from flask import request

from apis.APIModels.User import UserFields, UserCreateFields, UserUpdateFields
from apis.namespaces import user_api
from core.logic.Users import UserController
from core.ViewSchemas.User import *

ucon = UserController()


@user_api.route('/all')
class Users(Resource):
    @user_api.doc('list_users')
    @user_api.marshal_list_with(UserFields)
    def get(self):
        '''List all users.'''
        users = ucon.get_all()
        if users is None:
            return 'No users found.', 404

        return users_schema.dump(users)


@user_api.route('/create')
class User(Resource):
    @user_api.doc('create_user')
    @user_api.expect(UserCreateFields)
    @user_api.response(201, 'User Created.')
    @user_api.response(400, 'Failed to create user.')
    def post( self ):
        '''Create a user.'''
        new_user = ucon.create(
            username=request.json['username'],
            email=request.json['email'],
            password=request.json['password']
        )
        if new_user is None:
            return "Failed to create user.", 400
        # return the ma.schema version appropriate to show a user
        return user_schema.dump(new_user), 201


@user_api.route('/id/<id>')
@user_api.param('id', "The user's unique identifier.")
@user_api.response(404, 'User not found')
class User(Resource):
    @user_api.doc('get_user_id')
    def get(self, id):
        '''Fetch a user given its identifier.'''
        user = ucon.get_id(id=id)
        if user is None:
            return 'User not found.', 404
        return user_schema.dump(user)


@user_api.route('/username/<username>')
@user_api.param('username', "The user's username.")
@user_api.response(404, 'User not found')
class User(Resource):
    @user_api.doc('get_user_username')
    def get( self, username ):
        '''Fetch a user given its username.'''
        user = ucon.get_username( username=username )
        if user is None:
            return 'User not found.', 404
        return user_schema.dump(user)


@user_api.route('/email/<email>')
@user_api.param('email', "The user's email address.")
@user_api.response(404, 'User not found')
class User(Resource):
    @user_api.doc('get_user_email')
    def get( self, email ):
        '''Fetch a user given its email address.'''
        user = ucon.get_email( email=email )
        if user is None:
            return 'User not found.', 404
        return user_schema.dump( user )


@user_api.route('/uuid/<uuid>')
@user_api.param('uuid', "The user's UUID.")
@user_api.response(404, 'User not found.')
@user_api.response(code=200, model=UserFields, description='')
class User(Resource):
    @user_api.doc('get_user_uuid')
    def get( self, uuid ):
        '''Fetch a user given its UUID.'''
        user = ucon.get_uuid( uuid=uuid )
        if user is None:
            return 'User not found.', 404
        return user_schema.dump(user)

    @user_api.doc('update_user')
    @user_api.expect(UserUpdateFields)
    @user_api.response(404, 'User not found.')
    def put( self, uuid ):
        '''Update a user's attributes.'''

        user = ucon.get_uuid( uuid=uuid )
        if user is None:
            return "User not found.", 404

        username=None
        email=None
        password=None

        if 'username' in request.json:
            username=request.json['username']
        if 'email' in request.json:
            email=request.json['email']
        if 'password' in request.json:
            password=request.json['password']

        user_result = ucon.update( user, username, email, password )

        if user_result is None:
            return "Failed to update user.", 400
        # return the ma.schema version appropriate to show a user
        return user_schema.dump(user_result), 201