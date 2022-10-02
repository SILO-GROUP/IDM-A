from flask_restx import Resource
from modules.Sessions.Decorators import session_required
from modules.Pantheon.Namespaces import email_api as api
from modules.Groups.Decorators import require_group, in_group_or_superuser
from modules.Groups.Config import module_config as group_mappings
from .Controller import EmailController

email_controller = EmailController()


@api.route('/challenge/generate')
class EmailValidation(Resource):
    @session_required
    def post(self):
        '''Create or update a validation challenge.'''
        return "Not implemented.", 500


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
