from modules.Pantheon.Factory import ma
from modules.Emails.DatabaseModels import EmailValidationModel


class EmailChallengeSchema(ma.Schema):
    class Meta:
        model = EmailValidationModel
        fields = (
            "creation_date",
            "validation_token",
            "assoc_uuid"
        )


email_challenge_schema = EmailChallengeSchema()
email_challenge_schemas = EmailChallengeSchema(many=True)