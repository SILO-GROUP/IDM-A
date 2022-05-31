import configparser
import os

config = configparser.ConfigParser()

dir_path = os.path.dirname(os.path.realpath(__file__))
config_file_path = '{0}/../../config.ini'.format( dir_path )


class Config:
    def __init__(self):
        settings = configparser.ConfigParser(allow_no_value=True)
        settings.read( config_file_path )
        self.db_uri = settings.get('database', 'db_uri' )
        self.title = settings.get( 'branding', 'title' )
        self.version = settings.get( 'branding', 'version' )
        self.description = settings.get( 'branding', 'description' )


system_config = Config()