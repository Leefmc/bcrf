'''This module provides code for creating and interacting with Character
Guides.'''

# standard
# related
import Blender.Scene
# local
import bcrf.bcrf_lib.exceptions


def create_character_guide():
    '''Create a character guide in the scene, and return the character guide
    object.
    
    @return: A L{CharacterGuide} object.
    '''
    pass

class CharacterGuide(object):
    '''This class represents an existing Character Guide in the scene.'''

    def __init__(self, guide_name):
        '''
        @param guide_name: The name of an existing Guide.
        
        @see: To create a new Guide, see L{create_guide}.
        
        @raise CharacterGuideNotFoundError: see L{CharacterGuideNotFoundError}
        @raise NameNotCharacterGuideError: see L{NameNotCharacterGuideError}
        '''
        pass

class CharacterGuideNotFoundError(bcrf.bcrf_lib.exceptions.BCRFRigLibError):
    '''A character guide was going to be loaded, but was not found.'''
    pass

class NameNotCharacterGuideError(bcrf.bcrf_lib.exceptions.BCRFRigLibError):
    '''A name for a character guide was given, but it is either not a BCRF 
    Character Guide, or is not correctly formatted.'''
    pass

