from functools import wraps
from flask import g
from modules.Groups.GroupMappings import group_mappings


# returns true if user is in that group or in the superuser group
def in_group_or_superuser( user, group_name ):
    if group_name in [ usergroup.name for usergroup in user.groups ] or group_mappings.USERS_SUPERUSER in [usergroup.name for usergroup in user.groups]:
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
