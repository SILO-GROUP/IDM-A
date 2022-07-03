from flask_restx import Resource
from flask import request, g
from functools import wraps
from modules.Pantheon.Factory import app
from modules.Sessions.APIModels import SessionFields, SessionCreateFields, InsecureSessionFields
from modules.Pantheon.Namespaces import session_api as api
from modules.Sessions.Controller import session_controller
from modules.Sessions.ViewSchemas import session_schema, sessions_schema
from modules.Sessions.Decorators import session_required
from modules.Groups.Decorators import require_group
from modules.Groups.GroupMappings import group_mappings

@api.route('/all')
class Sessions(Resource):
    @session_required
    @require_group(group_mappings.SESSIONS_LIST_ALL)
    @api.marshal_list_with(InsecureSessionFields)
    def get(self):
        '''List all Sessions.'''
        sessions = session_controller.get_all()
        if sessions is None:
            return 'No sessions found.', 404

        return sessions_schema.dump(sessions)


@api.route('/create')
class Sessions(Resource):
    @api.no_session_required
    @api.doc('create_session')
    @api.expect(SessionCreateFields)
    @api.response(201, 'Session created.')
    @api.response(400, 'Failed to create session.')
    def post(self):
        '''Create a session.'''
        session = session_controller.create( uuid=request.json['uuid'], password=request.json['password'] )
        if session is None:
            return 'No session could be created.', 401

        return session_schema.dump(session), 201


@api.route('/suid/<suid>')
class Sessions(Resource):
    @session_required
    @api.doc('destroy_session')
    @api.expect(SessionCreateFields)
    @api.response(201, 'Session created.')
    @api.response(400, 'Failed to create session.')
    # don't use @require group, here.  Need to add check against target user to allow operation on same user as well
    # as to an administrative group.  not yet implemented.
    def delete(self):
        '''Destroy a session.'''
        session = session_controller.destroy( uuid=request.json['uuid'] )
        if session is None:
            return 'No session could be created.', 401

        return session_schema.dump(session), 201
