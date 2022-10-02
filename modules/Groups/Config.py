from modules.Pantheon.Config import system_config, Config

config_file_path = '{0}/groups.ini'.format( system_config.modules_conf_path )


class ModuleConfig(Config):
    def __init__(self):
        Config.__init__(self)
        self.parserobj.read( config_file_path )
        self.USERS_SUPERUSER = self.parserobj.get('users', 'SUPERUSER')
        self.USERS_LIST_ALL = self.parserobj.get( 'users', 'LIST_ALL' )
        self.USERS_DEACTIVATE = self.parserobj.get('users', 'DEACTIVATE')
        self.USERS_ACTIVATE = self.parserobj.get('users', 'ACTIVATE')
        self.USERS_MODIFY = self.parserobj.get('users', 'MODIFY')
        self.USERS_DELETE = self.parserobj.get('users', 'DELETE')
        self.GROUPS_LIST_ALL = self.parserobj.get('groups', 'LIST_ALL')
        self.GROUPS_CREATE = self.parserobj.get('groups', 'CREATE')
        self.GROUPS_SHOW_MEMBERS = self.parserobj.get('groups', 'SHOW_MEMBERS')
        self.GROUPS_MODIFY = self.parserobj.get('groups', 'MODIFY')
        self.GROUPS_DELETE =self.parserobj.get('groups', 'DELETE')
        self.GROUPS_MODIFY_MEMBERS = self.parserobj.get('groups', 'MODIFY_MEMBERS')
        self.SESSIONS_LIST_ALL = self.parserobj.get('sessions', 'LIST_ALL')
        self.SESSIONS_DESTROY = self.parserobj.get('sessions', 'DESTROY')
        self.EMAILS_LIST_ALL = self.parserobj.get('emails', 'LIST_ALL')


module_config = ModuleConfig()