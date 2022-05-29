from functools import wraps
from flask import g


def require_group(group_name):
    def group_wrapper(method):
        @wraps(method)
        def _impl(*method_args, **method_kwargs):
            if group_name in [usergroup.name for usergroup in g.session.user.groups] or 'wheel' in [usergroup.name for usergroup in g.session.user.groups]:
                return method(*method_args, **method_kwargs)
            else:
                return "User '{0}' is not in the group '{1}' to be authorized to perform this action.".format(
                    g.session.user.username, group_name
                ), 401
        return _impl
    return group_wrapper
