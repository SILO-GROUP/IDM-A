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
    suid = Column(String(37), default=generate_uuid, nullable=False, unique=True)
    creation_date = Column( TIMESTAMP, default=datetime.utcnow, nullable=False )

    # MTO
    owner_id = Column(String(37), ForeignKey('user.uuid', ondelete="CASCADE"), nullable=False, unique=True)
    # owner = relationship( 'UserModel', backref="sessions")
    # user = relationship( 'UserModel', back_populates="sessions" )
    # user = relationship( 'UserModel', backref="sessions" )
    UniqueConstraint( 'id', 'suid' )

    def __repr__(self):
        return '<Session %s>' % self.suid

