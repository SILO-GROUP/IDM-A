from modules.Pantheon.Factory import db
# from modules.Sessions.Associations import user_session_relations
from sqlalchemy import Column, Integer, String, UniqueConstraint, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime


def generate_uuid():
    return str(uuid.uuid4())


class SessionModel(db.Model):
    __tablename__ = 'session'

    id =  Column( Integer, primary_key=True, autoincrement=True, nullable=False )
    uuid = Column( String(37), name="uuid", default=generate_uuid, nullable=False, unique=True )
    creation_date = Column( TIMESTAMP, default=datetime.utcnow, nullable=False )

    user_uuid = Column( String(37), ForeignKey('user.uuid', ondelete="CASCADE" ), nullable=False, unique=True )
    # user = relationship( 'UserModel', back_populates="sessions" )
    # user = relationship( 'UserModel', backref="sessions" )
    UniqueConstraint( 'id', 'uuid' )

    def __repr__(self):
        return '<Session %s>' % self.uuid

