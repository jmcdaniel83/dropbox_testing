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

from datetime import datetime, timedelta
from typing import List, Dict
# @CUSTOMIZE  Add standard modules here.

# third-party modules
import dropbox

from dropbox.files import ListFolderResult, FileMetadata
# @CUSTOMIZE  Add third party modules here.

# custom modules
from .dropbox_config import DropboxConfig
from .file_data import FileData
# @CUSTOMIZE  Add custom modules here.

class DropboxApi:
    '''
    Will contain the methods that we care about when it comes to using the
    dropbox api.
    '''

    # the connection to dropbox
    _conn: dropbox.Dropbox = None

    def __init__( self, config: DropboxConfig ) -> None:
        '''
        Will create our connection to dropbox using the provided configuration.
        The connection will be used for all other calls to the dropbox api.
        '''
        self._conn = dropbox.Dropbox( config.access_token )

    def upload_file( self, file_path: str ) -> None:
        '''
        Will upload the provided file to dropbox.
        '''
        if file_path is None:
            logging.error( 'No file path provided.' )
            return

        try:
            # load the data and upload it to dropbox (read as binary)
            logging.info( f'uploading file [{file_path}]...' )
            with open( file_path, 'rb' ) as fin:
                self._conn.files_upload( fin.read(), f'/{file_path}' )

        except Exception as e:
            logging.error( f'Failed to upload file: {e}' )

    def delete_file( self, file_path: str ) -> None:
        '''
        Will delete the provided file from dropbox.
        '''
        if file_path is None:
            logging.error( 'No file path provided.' )
            return

        try:
            # load the data and upload it to dropbox
            logging.info( f'deleting file [{file_path}]...' )
            self._conn.files_delete( f'/{file_path}' )

        except Exception as e:
            logging.error( f'Failed to delete file: {e}' )

    def update_file( self, file_path: str ) -> None:
        '''
        Will update the provided file from dropbox.
        '''
        if file_path is None:
            logging.error( 'No file path provided.' )
            return

        try:
            # load the data and upload it to dropbox
            logging.info( f'updating file [{file_path}]...' )
            with open( file_path, 'rb' ) as fin:
                self._conn.files_upload(
                    fin.read(), f'/{file_path}',
                    mode=dropbox.files.WriteMode.overwrite
                )

        except Exception as e:
            logging.error( f'Failed to update file: {e}' )

    def get_files( self ) -> List[FileMetadata]:
        '''
        Will get all of the files from dropbox.
        '''
        try:
            # load the data and upload it to dropbox
            logging.info( f'getting files...' )
            files: ListFolderResult = self._conn.files_list_folder( '' )

            # provide back our file entries
            return files.entries

        except Exception as e:
            logging.error( f'Failed to get files: {e}' )

    def get_file_days( self ) -> List[FileData]:
        '''
        Will package all the found files from dropbox into simple objects that
        contain the amount of days they have existed.
        '''
        files = self.get_files()

        # go through the files and generate our objects
        file_data: List[FileData] = []
        for f in files:
            # get the amount of days this file has existed
            days = self.get_meta_days( f )

            # save our data
            file_data.append( FileData( f.path_display, days ) )

        return file_data

    def get_days( self, file_path: str ) -> int:
        '''
        Will check the date of the provided file from dropbox.
        '''
        if file_path is None:
            logging.error( 'No file path provided.' )
            return

        try:
            # load the data and upload it to dropbox
            logging.info( f'checking date of file [{file_path}]...' )
            meta_data = self._conn.files_get_metadata( f'/{file_path}' )

            return self._get_days( meta_data )

        except Exception as e:
            logging.error( f'Failed to check date of file: {e}' )

    def get_meta_days( self, file: FileMetadata ) -> int:
        return self._get_days( file )

    # -------------------------------------------------------------------------
    # Private Methods
    # -------------------------------------------------------------------------

    def _get_days( self, file: FileMetadata ) -> int:
        '''
        Will check the date of the provided file from dropbox.
        '''
        if file is None:
            logging.error( 'No file provided.' )
            return

        try:
            # check the amount of time that has passed since the file was last
            # modified
            file_time: datetime = file.server_modified
            current_time = datetime.now()

            # provide the number of days this file has been uploaded
            diff: timedelta = current_time - file_time
            return int( diff.days )

        except Exception as e:
            logging.error( f'Failed to check date of file: {e}' )

# EOF
