from modules.Emails.Config import module_config
from modules.Emails.DatabaseModels import EmailValidationModel
from modules.Pantheon.Factory import db
from sqlalchemy import exc
from modules.Users.Controller import user_controller

class EmailController:
    def __init__(self):
        pass

    def create_challenge(self, uuid):
        user = user_controller.get_uuid( uuid )
        if user is None:
            return False

        challenge = EmailValidationModel(assoc_uuid=user.uuid)
        if challenge is not None:
            try:
                db.session.add(challenge)
                db.session.commit()

            except exc.PendingRollbackError:
                return False
        else:
            return False

        # send a challenge email, but don't have challenge creation return status dependent on it
        # it is a separate function that can be re-triggered independently by the user or a member of an allowed group
        self.send_challenge( user.uuid, challenge )
        return True

    def send_challenge( self, uuid, challenge ):
        user = user_controller.get_uuid( uuid )
        if user is None:
            return False



        return False

    def validate_challenge(self):
        pass

    def get_all_challenges(self):
        challenges = EmailValidationModel.query.all()
        if challenges is None:
            return None
        return challenges

    def delete_challenge_token(self):
        pass


email_controller = EmailController()