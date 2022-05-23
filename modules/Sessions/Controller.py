from modules.Sessions.DatabaseModels import SessionModel
from modules.Users.Controller import UserController
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

    def create( self, uuid, password ):
        ucon = UserController()
        user = ucon.get_uuid( uuid )
        if user is None:
            return None

        try:
            session = SessionModel()
            db.session.add(session)
            db.session.commit()

            return session
        except exc.IntegrityError:
            return None
        except exc.PendingRollbackError:
            print("Constraint failure?")
            return None