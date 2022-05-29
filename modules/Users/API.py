from flask import request
from flask_restx import Resource

from modules.Users.APIModels import UserFields, UserCreateFields, UserUpdateFields
from modules.Pantheon.Namespaces import user_api as api
from modules.Users.Controller import user_controller
from modules.Users.ViewSchemas import user_schema, users_schema
from modules.Sessions.Decorators import require_session
from modules.Groups.Decorators import require_group
from modules.Users.Decorators import require_same_user


def expect_header( name, desc ):
    # user_api needs abstracted away here so that this can be reusable in a shared library for other namespaces
    return api.doc(params={ name: {'in': 'header', 'description':  desc } })


def input_schema( schema ):
    # user_api needs abstracted away here so that this can be reusable in a shared library for other namespaces
    return api.expect(schema)


def expect_url_var( variable, desc ):
    # user_api needs abstracted away here so that this can be reusable in a shared library for other namespaces
    return api.param( variable, desc )


def output_schema( schema ):
    # user_api needs abstracted away here so that this can be reusable in a shared library for other namespaces
    return api.marshal_list_with( schema, mask='' )


def potential_response( status_code, message ):
    # user_api needs abstracted away here so that this can be reusable in a shared library for other namespaces
    return api.response( status_code, message )


@api.route('/all')
class Users(Resource):
    @require_session
    @require_group('wheel')
    @expect_header( 'Authorization', 'An authorization bearer token.')
    @output_schema( UserFields )
    @potential_response( 404, 'No users found.' )
    @potential_response( 200, 'Success' )
    def get(self):
        '''List all users.'''
        users = user_controller.get_all()
        if users is None:
            return 'No users found.', 404

        return users_schema.dump(users)


@api.route('/create')
class User(Resource):
    @input_schema(UserCreateFields)
    @potential_response(201, 'User Created.')
    @potential_response(400, 'Failed to create user.')
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
@expect_url_var('id', "The user's unique identifier.")
@potential_response(404, 'User not found')
class User(Resource):
    @require_session
    @expect_header( 'Authorization', 'An authorization bearer token.')
    @require_group('wheel')
    @api.doc('get_user_id')
    def get( self, id ):
        '''Fetch a user given its identifier.'''
        user = user_controller.get_id(id=id)
        if user is None:
            return 'User not found.', 404
        return user_schema.dump(user)


@api.route('/username/<username>')
@api.param('username', "The user's username.")
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user_username')
    def get( self, username ):
        '''Fetch a user given its username.'''
        user = user_controller.get_username(username=username)
        if user is None:
            return 'User not found.', 404
        return user_schema.dump(user)


@api.route('/email/<email>')
@api.param('email', "The user's email address.")
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user_email')
    def get( self, email ):
        '''Fetch a user given its email address.'''
        user = user_controller.get_email(email=email)
        if user is None:
            return 'User not found.', 404
        return user_schema.dump( user )


@api.route('/uuid/<uuid>')
@api.param('uuid', "The user's UUID.")
@api.response(404, 'User not found.')
@api.response(code=200, model=UserFields, description='')
class User(Resource):
    @api.doc('get_user_uuid')
    @require_session
    def get( self, uuid ):
        '''Fetch a user given its UUID.'''
        user = user_controller.get_uuid(uuid=uuid)
        if user is None:
            return 'User not found.', 404
        return user_schema.dump(user)

    @api.doc('update_user')
    @require_session
    @require_same_user
    @api.expect(UserUpdateFields)
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