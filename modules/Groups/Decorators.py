from functools import wraps
from flask import g
from modules.Groups.Config import module_config


# returns true if user is in that group or in the superuser group
def in_group_or_superuser( user, group_name ):
    group_set = [ usergroup.name for usergroup in user.groups ]
    if group_name in group_set or module_config.USERS_SUPERUSER in group_set:
        return True
    else:
        return False


def require_group(group_name):
    def group_wrapper(method):
        @wraps(method)
        def _impl(*method_args, **method_kwargs):
            if in_group_or_superuser( g.session.user, group_name ):
                return method(*method_args, **method_kwargs)
            else:
                return "User '{0}' is not in the group '{1}' to be authorized to perform this action.".format(
                    g.session.user.username, group_name
                ), 401
        return _impl
    return group_wrapper
