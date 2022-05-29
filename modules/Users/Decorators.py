from modules.Pantheon.Factory import app
from flask import request, g
from modules.Sessions.Controller import session_controller
from functools import wraps


def require_same_user(method):
    @wraps(method)
    def _impl(*method_args, **method_kwargs):
        if g.session.user.uuid == method_kwargs['uuid']:
            return method(*method_args, **method_kwargs)
        else:
            return 'You are not authorized to perform this action on another user.', 401
    return _impl
