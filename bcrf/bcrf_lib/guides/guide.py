'''This module provides code for creating and interacting with Guides.'''

# standard
# related
import Blender.Scene
# local
import bcrf.rig_lib.exceptions


def create_guide():
    '''Create a guide in the scene, and return the guide object.
    
    @return: A L{Guide} object.
    '''
    pass

class Guide(object):
    '''This class represents an existing Guide in the scene.'''

    def __init__(self):
        '''Constructor
        '''
        pass

class GuideNotFoundError(bcrf.rig_lib.exceptions.BCRFRigLibError):
    '''A guide was going to be loaded, but was not found.'''
    pass

class NameNotGuideError(bcrf.rig_lib.exceptions.BCRFRigLibError):
    '''A name for a guide was given, but it is either not a BCRF Guide, or is
    not correctly formatted.'''
    pass

