from modules.Pantheon.Factory import db
from modules.Users.DatabaseModels import UserModel
from sqlalchemy import exc
# data validation happens _here_
# input sanitization happens here, too.


class UserController:
    def __init__(self):
        pass

    # fetch all users
    def get_all(self):
        users = UserModel.query.all()
        if users is None:
            return None
        return users

    # fetch a user object by id
    def get_id(self, id):
        user = UserModel.query.get(id)
        if user is None:
            return None
        return user

    # fetch a user object by username
    def get_username(self, username):
        user = UserModel.query.filter_by( username=username).first()
        if user is None:
            return None
        return user

    # fetch a user object by email
    def get_email( self, email ):
        user = UserModel.query.filter_by( email=email ).first()
        if user is None:
            return None
        return user

    # fetch a user object by uuid
    def get_uuid( self, uuid ):
        user = UserModel.query.filter_by(uuid=uuid).first()
        if user is None:
            return None
        return user

    # deactivate a user
    def deactivate( self, uuid ):
        user = self.get_uuid(uuid)
        if user is None:
            return None
        user.active = False
        db.session.commit()

    # activate a user
    def activate( self, uuid ):
        user = self.get_uuid(uuid)
        if user is None:
            return None
        user.active = True
        db.session.commit()

    # delete a user
    def delete( self, uuid ):
        user = self.get_uuid(uuid)
        if user is None:
            return None
        user.active = True
        db.session.commit()

    # create a user
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

    # update a user attribute
    def update( self, user, username=None, email=None, password=None ):
        if user is None:
            return None

        if username is not None:
            user.username = username
        if email is not None:
            user.email = email
        if password is not None:
            user.password = password

        try:
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


user_controller = UserController()
