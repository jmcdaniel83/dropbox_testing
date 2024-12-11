#!/usr/bin/env python
'''
@CUSTOMIZE  Place module documenation here.
'''

__author__ = 'Jason McDaniel'
__copyright__ = 'Copyright 2023, PlanComputer'
__credits__ = ['Jason McDaniel']
__license__ = 'Proprietary'
__version__ = '0.1.0'
__maintainer__ = 'Jason McDaniel'
__email__ = 'jaymac83@gmail.com'
__status__ = 'Prototype'

# standard modules
import logging
import os
import configparser
# @CUSTOMIZE  Add standard modules here.

# third-party modules
# @CUSTOMIZE  Add third party modules here.

# custom modules
# @CUSTOMIZE  Add custom modules here.

class Keys:
    # version section items
    VERSION = 'version'
    CONFIGFILE_VERSION = 'configfile_version'

    # keys section items
    KEYS = 'keys'
    OAUTH_APP_KEY = 'oauth_app_key'
    OAUTH_APP_SECRET = 'oauth_app_secret'
    OAUTH_REFRESH_TOKEN= 'oauth_refresh_token'
    OAUTH_ACCESS_TOKEN = 'oauth_access_token'

class DropboxConfig:

    # the raw configuration
    _config: dict = None

    @property
    def version( self ) -> str:
        return self._config[ Keys.VERSION ][ Keys.CONFIGFILE_VERSION ]

    @property
    def app_key( self ) -> str:
        return self._config[ Keys.KEYS ][ Keys.OAUTH_APP_KEY ]

    @property
    def app_secret( self ) -> str:
        return self._config[ Keys.KEYS ][ Keys.OAUTH_APP_SECRET ]

    @property
    def refresh_token( self ) -> str:
        return self._config[ Keys.KEYS ][ Keys.OAUTH_REFRESH_TOKEN ]

    @property
    def access_token( self ) -> str:
        return self._config[ Keys.KEYS ][ Keys.OAUTH_ACCESS_TOKEN ]

    def __init__( self, file_path: str ) -> None:
        '''
        Will load the configuration file and store all items for ease of access.
        '''
        config = self._load_configuration( file_path )

        # save the configuration parsed
        self._config = config

    def _load_configuration( self, file_path: str ) -> dict:
        '''
        Load an INI file for the configuration values needed to connect to dropbox.
        '''
        # the configuration we will provide
        config = {}

        obj = configparser.ConfigParser()
        with open( file_path, 'r' ) as fin:
            # read the file
            obj.read_file( fin )

            # go through our sections and load them into our configuation
            for section in obj.sections():
                items = obj.items( section )
                config[ section ] = dict( items )

        return config


# EOF
