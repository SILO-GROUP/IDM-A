from core.Pantheon.AppFactory import *
from core.ViewSchemas.User import user_schema, users_schema
from core.DatabaseModels.User import UserModel
from sqlalchemy import exc
# data validation happens _here_
# input sanitization happens here, too.


class UserController:
    def __init__(self):
        pass

    def get_all(self):
        users = UserModel.query.all()
        if users is None:
            return None
        return users

    def get_id(self, id):
        user = UserModel.query.get(id)
        if user is None:
            return None
        return user

    def get_username(self, username):
        user = db.session.query(UserModel).filter_by( username=username).first()
        if user is None:
            return None
        return user

    def get_email( self, email ):
        user = db.session.query(UserModel).filter_by( email=email ).first()
        if user is None:
            return None
        return user

    def get_uuid( self, uuid ):
        user = db.session.query(UserModel).filter_by( uuid=uuid ).first()
        if user is None:
            return None
        return user

    def create(self, username, email, password):
        try:
            user = UserModel(
                username=username,
                email=email,
                password=password
            )
            db.session.add(user)

            db.session.commit()
            return user
        except exc.IntegrityError:
            return None
        except exc.PendingRollbackError:
            print("Unique Constraint failure...")
            return None

    def update( self, user, username=None, email=None, password=None ):
        if user is None:
            return None
        try:
            if username is not None:
                user['username'] = username
            if email is not None:
                user['email'] = email
            if password is not None:
                user['password'] = password
            db.session.commit()
            return user
        except exc.IntegrityError:
            return None

    # returns true if the user has that field set to that value
    def has_field_value( self, user, attribute, value ):
        pass

    def is_active( self, user ):
        pass

    def email_verified( self, user ):
        pass