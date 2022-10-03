from flask_restx import Resource
from modules.Sessions.Decorators import session_required
from modules.Pantheon.Namespaces import email_api as api
from modules.Groups.Decorators import require_group, in_group_or_superuser
from modules.Groups.Config import module_config as group_mappings
from modules.Emails.Controller import email_controller
from modules.Users.Controller import user_controller
from modules.Emails.ViewSchemas import email_challenge_schema

@api.route('/challenge/generate/<uuid>')
@api.expect_url_var('uuid', 'The user UUID to create the challenge for.')
class EmailValidation(Resource):
    @session_required
    def post(self, uuid):
        '''Create or update a validation challenge.'''
        target_user = user_controller.get_uuid( uuid )
        if target_user is not None:
            new_challenge = email_controller.create_challenge( uuid=target_user.uuid )

            if new_challenge is None:
                return "Failed to create challenge.", 500

            return email_challenge_schema.dump( new_challenge )
        else:
            return "User not found.", 404


@api.route('/challenge/send')
class EmailValidation(Resource):
    @session_required
    def post(self):
        '''Send a previously generated validation challenge.'''
        return "Not implemented.", 500


@api.route('/challenge/answer/<token>')
class EmailValidation(Resource):
    @session_required
    def get(self):
        '''Answer a validation challenge.'''
        return "Not implemented.", 500


@api.route('/challenge/list')
class EmailValidation(Resource):
    @require_group( group_mappings.EMAILS_LIST_ALL )
    def get(self):
        '''List all validation challenges.'''
        return "Not implemented.", 500


@api.route('/challenge/delete/<token>')
class EmailValidation(Resource):
    def get(self):
        '''Delete a validation challenge.'''
        return "Not implemented.", 500
