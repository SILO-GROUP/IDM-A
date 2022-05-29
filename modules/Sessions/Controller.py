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

    def create( self, uuid, password ):
        user = user_controller.get_uuid( uuid )
        if user is None:
            print("User not found.")
            return None
        else:
            print(user)

        try:
            session = SessionModel(owner_id=user.uuid)
            db.session.add(session)
            db.session.commit()

            return session
 #       except exc.IntegrityError:
 #           print("Integrity error...")
 #           return None
        except exc.PendingRollbackError:
            print("Constraint failure?")
            return None

    def get_token( self, token ):
        session = db.session.query(SessionModel).filter_by( suid=token ).first()
        return session


session_controller = SessionController()
