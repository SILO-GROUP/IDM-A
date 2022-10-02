import configparser
import os

config = configparser.ConfigParser()

dir_path = os.path.dirname(os.path.realpath(__file__))
config_file_path = '{0}/../../config.ini'.format( dir_path )


class Config:
    def __init__(self):
        self.parserobj = configparser.ConfigParser(allow_no_value=True)
        self.parserobj.read( config_file_path )
        self.db_uri = self.parserobj.get('database', 'db_uri' )
        self.title = self.parserobj.get( 'branding', 'title' )
        self.version = self.parserobj.get( 'branding', 'version' )
        self.description = self.parserobj.get( 'branding', 'description' )
        self.modules_conf_path = '{0}/../../{1}'.format( dir_path, self.parserobj.get('modules', 'confs_path') )
        self.port = self.parserobj.get('API', 'port')
        self.bind_addr = self.parserobj.get('API', 'bind_addr')
        self.debug = self.parserobj.getboolean('API', 'debug')
        self.environment = self.parserobj.get('API', 'environment')


system_config = Config()