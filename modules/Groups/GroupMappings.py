import configparser
from modules.Pantheon.Config import system_config

config_file_path = '{0}/groups.ini'.format( system_config.modules_conf_path )
print(config_file_path)


class GroupMappings:
    def __init__(self):
        settings = configparser.ConfigParser(allow_no_value=True)
        settings.read( config_file_path )
        self.USERS_SUPERUSER = settings.get('users', 'SUPERUSER')
        self.USERS_LIST_ALL = settings.get( 'users', 'LIST_ALL' )
        self.USERS_DEACTIVATE = settings.get('users', 'DEACTIVATE')
        self.USERS_ACTIVATE = settings.get('users', 'ACTIVATE')
        self.USERS_MODIFY = settings.get('users', 'MODIFY')
        self.USERS_DELETE = settings.get('users', 'DELETE')
        self.GROUPS_LIST_ALL = settings.get('groups', 'LIST_ALL')
        self.GROUPS_CREATE = settings.get('groups', 'CREATE')
        self.GROUPS_SHOW_MEMBERS = settings.get('groups', 'SHOW_MEMBERS')
        self.GROUPS_MODIFY =settings.get('groups', 'MODIFY')
        self.GROUPS_DELETE =settings.get('groups', 'DELETE')
        self.GROUPS_MODIFY_MEMBERS = settings.get('groups', 'MODIFY_MEMBERS')



group_mappings = GroupMappings()