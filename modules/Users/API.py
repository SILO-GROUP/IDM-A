from flask import request
from flask_restx import Resource

from modules.Users.APIModels import UserFields, UserCreateFields, UserUpdateFields
from modules.Pantheon.Namespaces import user_api as api
from modules.Users.Controller import user_controller
from modules.Users.ViewSchemas import user_schema, users_schema
from modules.Sessions.Decorators import require_session
from modules.Groups.Decorators import require_group
from modules.Users.Decorators import require_same_user


@api.route('/all')
class Users(Resource):
    @require_session
    @require_group('sys-enumerate_users')
#    @api.expect_header( 'Authorization', 'An authorization bearer token.')
    @api.output_schema( UserFields )
    @api.response( 404, 'No users found.' )
    @api.response( 200, 'Success' )
    def get(self):
        '''List all users.'''
        users = user_controller.get_all()
        if users is None:
            return 'No users found.', 404

        return users_schema.dump(users)


@api.route('/create')
class User(Resource):
    @api.no_auth()
    @api.input_schema(UserCreateFields)
    @api.response(201, 'User Created.')
    @api.response(400, 'Failed to create user.')
    def post( self ):
        '''Create a user.'''
        new_user = user_controller.create(
            username=request.json['username'],
            email=request.json['email'],
            password=request.json['password']
        )
        if new_user is None:
            return "Failed to create user.", 400
        # return the ma.schema version appropriate to show a user
        return user_schema.dump(new_user), 201


# require wheel to prevent enumeration of users
@api.route('/id/<id>')
@api.expect_url_var('id', "The user's unique identifier.")
class User(Resource):
    @require_session
    @require_group('wheel')
    @api.expect_header( 'Authorization', 'An authorization bearer token.')
    @api.response(404, 'User not found')
    @api.response(200, 'Success')
    def get( self, id ):
        '''Fetch a user given its identifier.'''
        user = user_controller.get_id(id=id)
        if user is None:
            return 'User not found.', 404
        return user_schema.dump(user)


@api.route('/username/<username>')
@api.param('username', "The user's username.")
@api.response(404, 'User not found')
@api.response(200, 'Success')
class User(Resource):
    @api.no_auth
    def get( self, username ):
        '''Fetch a user given its username.'''
        user = user_controller.get_username(username=username)
        if user is None:
            return 'User not found.', 404
        return user_schema.dump(user)


@api.route('/email/<email>')
@api.expect_url_var('email', "The user's email address.")
@api.response(404, 'User not found')
@api.response(200, model=UserFields, description='Success')
class User(Resource):
    def get( self, email ):
        '''Fetch a user given its email address.'''
        user = user_controller.get_email(email=email)
        if user is None:
            return 'User not found.', 404
        return user_schema.dump( user )


@api.route('/uuid/<uuid>')
@api.expect_url_var('uuid', "The user's UUID.")
@api.response(404, 'User not found.')
@api.response(code=200, model=UserFields, description='')
class User(Resource):
    @require_session
    def get( self, uuid ):
        '''Fetch a user given its UUID.'''
        user = user_controller.get_uuid(uuid=uuid)
        if user is None:
            return 'User not found.', 404
        return user_schema.dump(user)

    @require_session
    @require_same_user
    @api.input_schema(UserUpdateFields)
    @api.response(404, 'User not found.')
    def put( self, uuid ):
        '''Update a user's attributes.'''

        user = user_controller.get_uuid(uuid=uuid)
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

        user_result = user_controller.update(user, username, email, password)

        if user_result is None:
            return "Failed to update user.", 400
        # return the ma.schema version appropriate to show a user
        return user_schema.dump(user_result), 201