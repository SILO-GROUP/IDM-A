from modules.Pantheon.Factory import db
from modules.Sessions.DatabaseModels import SessionModel
from modules.Users.Controller import user_controller
from sqlalchemy import exc
# data validation happens _here_
# input sanitization happens here, too.


class SessionController:
    def __init__(self):
        pass

    def get_all(self):
        sessions = SessionModel.query.all()
        if sessions is None:
            return None
        return sessions

    def create( self, password, uuid=None, username=None ):
        if uuid is None and username is None:
            return None

        if uuid is None and username is not None:
            user = user_controller.get_username( username )

        if username is None and uuid is not None:
            user = user_controller.get_uuid( uuid )

        if user is None:
            return None
        else:
            if user.password != password:
                return None

        try:
            session = SessionModel(owner_id=user.uuid)
            db.session.add(session)
            db.session.commit()

            return session
        except exc.PendingRollbackError:
            return None

    def get_token(self, suid):
        session = db.session.query(SessionModel).filter_by(suid=suid).first()
        return session

    def destroy(self, suid):
        session = self.get_token( suid )
        if session is None:
            return None
        try:
            db.session.delete(session)
            db.session.commit()
            return True
        except exc.IntegrityError:
            return False


session_controller = SessionController()
