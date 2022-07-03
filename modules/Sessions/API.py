from flask_restx import Resource
from flask import request
from modules.Sessions.APIModels import SessionFields, SessionCreateFields, InsecureSessionFields
from modules.Pantheon.Namespaces import session_api as api
from modules.Sessions.Controller import session_controller
from modules.Sessions.ViewSchemas import session_schema, sessions_schema
from modules.Sessions.Decorators import session_required
from modules.Groups.Decorators import require_group, in_group_or_superuser
from modules.Groups.GroupMappings import group_mappings
from flask import g


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
    @api.expect_url_var('suid', 'The session ID to destroy.')
    @api.response(200, 'Session destroyed.')
    @api.response(400, 'Failed to create session.')
    # don't use @require group, here.  Need to add check against target user to allow operation on same user as well
    # as to an administrative group.  not yet implemented.
    def delete(self, suid):
        '''Destroy a session.'''
        #1. Fetch caller UUID
        #2. Fetch target session's user's UUID
        #3. If same, allow.
        #4. If not, check for group membership allowance or superuser.
        #5. If any, allow.  If none, deny.
        caller = g.session.user
        if caller is None:
            return "Invalid session used to call method.", 401

        target_session = session_controller.get_token( suid=suid )
        if target_session is None:
            return "Session being operated on was not found.", 404

        target = target_session.user

        allowed = False

        if caller.uuid == target.uuid:
            allowed = True
        if in_group_or_superuser( caller, group_mappings.SESSIONS_DESTROY ):
            allowed = True

        if allowed:
            result = session_controller.destroy( suid )
            if not result:
                return "Could not destroy session.", 401

        return None, 200
