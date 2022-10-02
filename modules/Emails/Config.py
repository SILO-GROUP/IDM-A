from modules.Pantheon.Config import Config, dir_path, config_file_path


class ModuleConfig(Config):
    def __init__(self):
        Config.__init__(self)
        self.send_validation_email = self.parserobj.get('email', 'send_validation_email')

        self.smtp_server = self.parserobj.get('email', 'server')
        self.smtp_port = self.parserobj.get('email', 'port')
        self.smtp_usetls = self.parserobj.get('email', 'usetls')


module_config = ModuleConfig()