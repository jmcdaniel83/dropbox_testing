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
import tarfile
# @CUSTOMIZE  Add standard modules here.

# third-party modules
# @CUSTOMIZE  Add third party modules here.

# custom modules
# @CUSTOMIZE  Add custom modules here.

class Archive:

    @classmethod
    def archive_folder( cls, source: str ) -> str:
        '''
        Will archive the provided folder into a tar.gz file.  The generated
        file will be placed in the same folder as the source folder. The name
        associated with our tar gz file will be returned for reference.
        '''

        # get our destination based off of the source
        base_name, _ = os.path.splitext( source )
        dest = f'{base_name}.tar.gz'

        logging.info( f'generating tar.gz file for {source} -> {dest}' )
        with tarfile.open( dest, 'w:gz' ) as tar:
            tar.add( source, arcname=os.path.basename( source ) )

        return dest

    @classmethod
    def archive_file( cls, source: str ) -> str:
        '''
        Will archive the provided file into a tar.gz file.  The generated
        file will be placed in the same folder as the source folder. The name
        associated with our tar gz file will be returned for reference.
        '''
        return cls.archive_folder( source )

# EOF
