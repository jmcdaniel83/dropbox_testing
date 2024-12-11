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
# @CUSTOMIZE  Add standard modules here.

# third-party modules
from dotenv import load_dotenv
# @CUSTOMIZE  Add third party modules here.

# custom modules
# @CUSTOMIZE  Add custom modules here.

class EnvConfig:
    '''
    The configuration items that we care about for the backup application.
    '''

    # --------------------------------------------------------------------------
    # Environment Configuration
    # --------------------------------------------------------------------------

    _envirionment: str = None
    _spire_dev_flag: bool = None

    # --------------------------------------------------------------------------
    # Drivers Configuration
    # --------------------------------------------------------------------------

    _volume_driver: str = None
    _networks_driver: str = None

    # --------------------------------------------------------------------------
    # MySql Configuration
    # --------------------------------------------------------------------------

    _maria_db_host: str = None
    _maria_db: str = None
    _maria_user: str = None
    _maria_password: str = None
    _maria_port: int = None
    _maria_root_password: str = None
    _maria_data_path: str = None

    _innodb_buffer_pool_size: str = None

    # --------------------------------------------------------------------------
    # Server Configuration
    # --------------------------------------------------------------------------

    _server_puid: int = None
    _server_pgid: int = None
    _server_timezone: str = None
    _server_ssh_port: int = None
    _server_password: str = None

    # --------------------------------------------------------------------------
    # phpmyadmin Configuration
    # --------------------------------------------------------------------------

    _phpmyadmin_username: str = None
    _phpmyadmin_password: str = None

    # --------------------------------------------------------------------------
    # peqeditor Configuration
    # --------------------------------------------------------------------------

    _peqeditor_password: str = None

    # --------------------------------------------------------------------------
    # ftp Configuration
    # --------------------------------------------------------------------------

    _ftp_quests_password: str = None

    # --------------------------------------------------------------------------
    # Misc Configuration
    # --------------------------------------------------------------------------

    _ip_address: str = None

    # --------------------------------------------------------------------------
    # Zone Configuration
    # --------------------------------------------------------------------------

    # Zone count you want to support: zones + 7000
    _port_range_high: int = None

    # --------------------------------------------------------------------------
    # Timezone Configuration
    # --------------------------------------------------------------------------

    _timezone: str = None

    # --------------------------------------------------------------------------
    # Dropbox Backups Configuration (optional)
    # --------------------------------------------------------------------------

    _deployment_name: str = None
    _backup_retention_days_database: int = None
    _backup_retention_days_deployment: int = None
    _backup_retention_days_quest: int = None

    # --------------------------------------------------------------------------
    # Accessor Methods
    # --------------------------------------------------------------------------

    ## environment
    @property
    def envirionment( self ) -> str: return self._envirionment

    @property
    def is_spire( self ) -> bool: return self._spire_dev_flag

    ## drivers
    @property
    def volume_driver( self ) -> str: return self._volume_driver

    @property
    def networks_driver( self ) -> str: return self._networks_driver

    ## mysql
    @property
    def maria_data_path( self ) -> str: return self._maria_data_path

    @property
    def maria_db_host( self ) -> str: return self._maria_db_host

    @property
    def maria_db( self ) -> str: return self._maria_db

    @property
    def maria_user( self ) -> str: return self._maria_user

    @property
    def maria_password( self ) -> str: return self._maria_password

    @property
    def maria_port( self ) -> int: return self._maria_port

    @property
    def maria_root_password( self ) -> str: return self._maria_root_password

    @property
    def innodb_buffer_pool_size( self ) -> str: return self._innodb_buffer_pool_size

    ## server
    @property
    def server_puid( self ) -> int: return self._server_puid

    @property
    def server_pgid( self ) -> int: return self._server_pgid

    @property
    def server_timezone( self ) -> str: return self._server_timezone

    @property
    def server_ssh_port( self ) -> int: return self._server_ssh_port

    @property
    def server_password( self ) -> str: return self._server_password

    ## phpmyadmin
    @property
    def phpmyadmin_username( self ) -> str: return self._phpmyadmin_username

    @property
    def phpmyadmin_password( self ) -> str: return self._phpmyadmin_password

    ## peqeditor
    @property
    def peqeditor_password( self ) -> str: return self._peqeditor_password

    ## ftp
    @property
    def ftp_quests_password( self ) -> str: return self._ftp_quests_password

    ## misc
    @property
    def ip_address( self ) -> str: return self._ip_address

    ## zone
    @property
    def port_range_high( self ) -> int: return self._port_range_high

    ## timezone
    @property
    def timezone( self ) -> str: return self._timezone

    ## dropbox backups (optional)
    @property
    def deployment_name( self ) -> str: return self._deployment_name

    @property
    def backup_retention_days_database( self ) -> int: return self._backup_retention_days_database

    @property
    def backup_retention_days_deployment( self ) -> int: return self._backup_retention_days_deployment

    @property
    def backup_retention_days_quest( self ) -> int: return self._backup_retention_days_quest

    # --------------------------------------------------------------------------
    # Internal Methods
    # --------------------------------------------------------------------------

    def __init__( self ) -> None:
        load_dotenv()

        # go through and set our properties
        ## environment
        self._envirionment = os.getenv( 'ENV' )
        self._spire_dev_flag = os.getenv( 'SPIRE_DEV' )

        ## drivers
        self._volume_driver = os.getenv( 'VOLUMES_DRIVER' )
        self._networks_driver = os.getenv( 'NETWORKS_DRIVER' )

        ## mysql
        self._maria_data_path = os.getenv( 'DATA_PATH_HOST' )
        self._maria_db_host = os.getenv( 'MARIADB_HOST', 'mariadb' )
        self._maria_db = os.getenv( 'MARIADB_DATABASE' )
        self._maria_user = os.getenv( 'MARIADB_USER' )
        self._maria_password = os.getenv( 'MARIADB_PASSWORD' )
        self._maria_port = os.getenv( 'MARIADB_PORT' )
        self._maria_root_password = os.getenv( 'MARIADB_ROOT_PASSWORD' )

        # the buffer pool size (defaulted to 256MB)
        self._innodb_buffer_pool_size = os.getenv( 'INNODB_BUFFER_POOL_SIZE', '256MB' )

        ## server
        self._server_puid = os.getenv( 'SERVER_PUID' )
        self._server_pgid = os.getenv( 'SERVER_PGID' )
        self._server_timezone = os.getenv( 'SERVER_TIMEZONE' )
        self._server_ssh_port = os.getenv( 'SERVER_SSH_PORT' )
        self._server_password = os.getenv( 'SERVER_PASSWORD' )

        ## phpmyadmin
        self._phpmyadmin_username = os.getenv( 'PHPMYADMIN_USERNAME' )
        self._phpmyadmin_password = os.getenv( 'PHPMYADMIN_PASSWORD' )

        ## peqeditor
        self._peqeditor_password = os.getenv( 'PEQ_EDITOR_PASSWORD' )

        ## ftp
        self._ftp_quests_password = os.getenv( 'FTP_QUESTS_PASSWORD' )

        ## misc
        self._ip_address = os.getenv( 'IP_ADDRESS' )

        ## zone
        self._port_range_high = os.getenv( 'PORT_RANGE_HIGH' )

        ## timezone
        self._timezone = os.getenv( 'TZ' )

        ## dropbox backups (optional)
        # used in backup names
        self._deployment_name = os.getenv( 'DEPLOYMENT_NAME', 'vulcan-local' )
        # how many days to keep backups (with defaults)
        self._backup_retention_days_database = os.getenv( 'BACKUP_RETENTION_DAYS_DB_SNAPSHOTS', 10 )
        self._backup_retention_days_deployment = os.getenv( 'BACKUP_RETENTION_DAYS_DEPLOYMENT', 35 )
        self._backup_retention_days_quest = os.getenv( 'BACKUP_RETENTION_DAYS_QUEST_SNAPSHOTS', 7 )

# EOF
