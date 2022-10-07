from flask_restx import Resource
from modules.Sessions.Decorators import session_required
from modules.Pantheon.Namespaces import email_api as api
from modules.Groups.Decorators import require_group, in_group_or_superuser
from modules.Groups.Config import module_config as group_mappings
from modules.Emails.Controller import email_controller
from modules.Users.Controller import user_controller
from modules.Emails.ViewSchemas import email_challenge_schema, email_challenge_schemas
from flask import g


@api.route('/challenge/generate/<uuid>')
@api.expect_url_var('uuid', 'The user UUID to create the challenge for.')
class EmailValidation(Resource):
    @session_required
    def post(self, uuid):
        '''Create or update a validation challenge.'''
        target_user = user_controller.get_uuid( uuid )
        if target_user is not None:
            if target_user.email_verified:
                return "This account's email address is already verified.", 304

            new_challenge = email_controller.create_challenge( uuid=target_user.uuid )

            if new_challenge is None:
                return "Failed to create challenge.", 500

            return email_challenge_schema.dump( new_challenge )
        else:
            return "User not found.", 404


@api.route('/challenge/answer/<token>')
class EmailValidation(Resource):
    def get(self, token):
        '''Answer a validation challenge.'''
        challenge = email_controller.get_challenge_by_token( token )
        if challenge is None:
            return "Invalid token.", 404

        if email_controller.validate_challenge( challenge ):
            return "Challenge validated.", 200
        else:
            return "Could not validate.", 401
