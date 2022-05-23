from core.Pantheon.AppFactory import db
from core.Groups.Associations import user_group_relations
from core.Sessions.Associations import user_session_relations
from sqlalchemy.orm import relationship
from sqlalchemy import UniqueConstraint, Boolean, Column, Integer, String, TIMESTAMP
import uuid
from datetime import datetime

# db.Model = DB Interface, Table Structure
# api.model = Tells Swagger what to use w/ @api.expect
#   or @api.marshal_list_with
# ma.Schema = Determines what fields are shown of the
#   object to the user

# impl:
# 1. tell swagger
# w/ @api.expect / @api.marshal* + api.model type variable
# 2. create an object of type db.model
# 3. inter


def generate_uuid():
    return str(uuid.uuid4())


# the model to interface with the database
class UserModel(db.Model):
    __tablename__ = 'user'

    id = Column( Integer, primary_key=True, autoincrement=True, nullable=False )
    uuid = Column( String(37), name="uuid", default=generate_uuid, nullable=False, unique=True )
    email = Column( String(100), nullable=False, unique=True )
    username =  Column( String(50), unique=True, nullable=False )
    password = Column( String(100), nullable=False )
    active = Column( Boolean(), default=False, )
    email_verified = Column( Boolean(), default=False )
    identity_verified = Column( Boolean(), default=False )
    creation_date = Column( TIMESTAMP, default=datetime.utcnow, nullable=False )
    UniqueConstraint( 'id', 'username', 'uuid', 'email' )
    groups = relationship( 'GroupModel', secondary=user_group_relations, back_populates="members" )
    sessions = relationship( 'SessionModel', secondary=user_session_relations, back_populates="user" )

    def __repr__(self):
        return '<User %s>' % self.uuid
