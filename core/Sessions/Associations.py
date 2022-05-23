from core.Pantheon import db
from sqlalchemy import Column, Table, ForeignKey, TIMESTAMP
from datetime import datetime

user_session_relations = Table(
    'user_session_assoc',
    db.metadata,
    Column('user_uuid', ForeignKey( 'user.uuid' ), primary_key=True ),
    Column('session_uuid', ForeignKey( 'session.uuid'), primary_key=True ),
    Column( TIMESTAMP, name='creation_date', default=datetime.utcnow, nullable=False )
)