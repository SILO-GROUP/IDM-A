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


group_mappings = GroupMappings()