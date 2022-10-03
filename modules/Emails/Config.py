from modules.Pantheon.Config import Config, dir_path, config_file_path


class ModuleConfig(Config):
    def __init__(self):
        Config.__init__(self)
        self.send_validation_email = self.parserobj.get('email', 'send_validation_email')

        self.smtp_server = self.parserobj.get('email', 'server')
        self.smtp_port = self.parserobj.getint('email', 'port')
        self.smtp_use_tls = self.parserobj.getboolean('email', 'use_tls')
        self.smtp_use_ssl = self.parserobj.getboolean('email', 'use_ssl')
        self.smtp_username = self.parserobj.get('email', 'username')
        self.smtp_password = self.parserobj.get('email', 'password')
        self.registration_reply_address = self.parserobj.get('email', 'registration_reply_address')


module_config = ModuleConfig()