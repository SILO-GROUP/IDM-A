from modules.Pantheon.Factory import db
from sqlalchemy import Column, Integer, String, UniqueConstraint, TIMESTAMP
import uuid
from datetime import datetime
from modules.Groups.Associations import user_group_relations
from sqlalchemy.orm import relationship


def generate_uuid():
    return str(uuid.uuid4())


class GroupModel(db.Model):
    __tablename__ = 'group'

    id =  Column( Integer, primary_key=True, autoincrement=True, nullable=False )
    uuid = Column( String(37), name="uuid", default=generate_uuid, nullable=False, unique=True )
    name = Column( String(100), unique=True, nullable=False )

    creation_date = Column( TIMESTAMP, default=datetime.utcnow, nullable=False )

    UniqueConstraint( 'id', 'uuid', 'name' )

    members = relationship( 'UserModel', secondary=user_group_relations, back_populates="groups" )

    def __repr__(self):
        return '<Group %s>' % self.uuid

