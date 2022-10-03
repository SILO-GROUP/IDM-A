from modules.Emails.Config import module_config
from modules.Emails.DatabaseModels import EmailValidationModel
from modules.Pantheon.Factory import db, app
from sqlalchemy import exc
from modules.Users.Controller import user_controller
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = module_config.smtp_server
app.config['MAIL_PORT'] = module_config.smtp_port
app.config['MAIL_USERNAME'] = module_config.smtp_username
app.config['MAIL_PASSWORD'] = module_config.smtp_password
app.config['MAIL_USETLS'] = module_config.smtp_use_tls
app.config['MAIL_USESSL'] = module_config.smtp_use_ssl
mail_controller = Mail(app)


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
        self.send_challenge( user.uuid, challenge.validation_token )
        return True

    def send_challenge( self, uuid, challenge_token ):
        user = user_controller.get_uuid( uuid )
        if user is None:
            return False

        challenge = email_controller.get_challenge_by_token( token=challenge_token )
        if challenge is None:
            return False


        msg_subject = "Your user activation on {0}".format( module_config.title )
        msg_body = 'Thanks for signing up for a user on {0}.\n\nYour activation URL is {1}.'.format(
                module_config.title,
                "{0}/email/challenge/answer/{1}".format(
                    module_config.external_base_url,
                    challenge.validation_token
                )
        )

        msg = Message(
            subject=msg_subject,
            body=msg_body,
            sender=module_config.registration_reply_address,
            recipients=[user.email]
        )

        result = mail_controller.send(msg)

        return True

    def validate_challenge(self):
        pass

    def get_all_challenges(self):
        challenges = EmailValidationModel.query.all()
        if challenges is None:
            return None
        return challenges

    def get_challenge_by_token( self, token ):
        challenge = EmailValidationModel.query.filter_by( validation_token=token ).first()
        if challenge is None:
            return None
        return challenge

    def delete_challenge_token(self):
        pass


email_controller = EmailController()