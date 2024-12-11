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
# @CUSTOMIZE  Add third party modules here.

# custom modules
# @CUSTOMIZE  Add custom modules here.

class FileData:

    '''
    The file path associated with this file
    '''
    _file_path: str = None

    '''
    The number of days this file has existed
    '''
    _days: int = None

    @property
    def file_path( self ) -> str:
        return self._file_path

    @property
    def days( self ) -> int:
        return self._days

    def __init__( self, file_path: str, days: int ) -> None:
        '''
        Will create a new instance of the FileData class.
        '''
        self._file_path = file_path
        self._days = days

# EOF
