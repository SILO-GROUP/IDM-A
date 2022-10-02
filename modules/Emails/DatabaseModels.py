from modules.Pantheon.Factory import db
from sqlalchemy import Column
import uuid
from datetime import datetime


def generate_uuid():
    return str(uuid.uuid4())


class EmailValidationModel(db.Model):
    __tablename__ = 'validation_emails'

    id =  Column( Integer, primary_key=True, autoincrement=True, nullable=False )
    creation_date = Column( TIMESTAMP, default=datetime.utcnow, nullable=False )
    validation_token  = Column(String(37), name="validation_token", default=generate_uuid, nullable=False, unique=True)
    assoc_uuid  = Column(Integer, ForeignKey('user.uuid'), unique=True, nullable=False)

    UniqueConstraint( 'id', 'assoc_uuid', 'validation_token' )

    def __repr__(self):
        return '<Group %s>' % self.guid

