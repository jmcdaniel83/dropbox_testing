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
__status__ = 'Prototype'

# standard modules
import logging
import os
import argparse
# @CUSTOMIZE  Add standard modules here.

# third-party modules
# @CUSTOMIZE  Add third party modules here.

# custom modules
from common import DropboxConfig, DropboxApi, Archive, EnvConfig
# @CUSTOMIZE  Add custom modules here.


def main():
    '''
    Main entry point for the script.
    '''
    # get our configuration
    config = DropboxConfig( 'config/vulcan.ini' )

    # our test file
    file_path = 'test_file.txt'

    # test our archive
    tar_file = Archive.archive_file( file_path )

    # get our api object
    api = DropboxApi( config )

    file_data = api.get_file_days()

    # backup our test file
    api.upload_file( tar_file )

    # delete our test file
    #api.delete_file( file_path )
    #api.delete_file( tar_file )

if __name__ == '__main__':
    # setup our logging
    format_str = '[{asctime}] :: [{levelname:^8}] :: [{name:<10}] - {message}'
    logging.basicConfig( format=format_str, style='{', level=logging.INFO )

    # load the .env file
    env_config = EnvConfig()

    # run our main function
    main()

# EOF
