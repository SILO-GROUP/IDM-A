from modules.Pantheon.Factory import app
from flask import request, g
from modules.Sessions.Controller import session_controller
from functools import wraps


@app.before_request
def fetch_requestor_context():
    g.context_flag = True

    auth_header = request.headers.get('Authorization')
    if auth_header and len( auth_header.split(" ") ) == 2:
        token = auth_header.split(" ")[1]
    else:
        token = ''
        g.session = None
    if token:
        g.session = session_controller.get_token( token=token )


def require_session(method):
    @wraps(method)
    def _impl(*method_args, **method_kwargs):
        if g.session is not None:
            return method(*method_args, **method_kwargs)
        else:
            return 'Requires an active session.', 403
    return _impl
