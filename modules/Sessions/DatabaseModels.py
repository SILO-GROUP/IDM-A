from modules.Pantheon.Factory import db
from modules.Sessions.Associations import user_session_relations
from sqlalchemy import Column, Integer, String, UniqueConstraint, TIMESTAMP
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

    UniqueConstraint( 'id', 'uuid' )

    user = relationship( 'UserModel', secondary=user_session_relations, back_populates="sessions" )

    def __repr__(self):
        return '<Session %s>' % self.uuid

