'''This module provides code for creating and interacting with Character
Guides.'''

# standard
# related
import Blender.Scene
# local
import bcrf.bcrf_lib.exceptions



class CharacterGuide(object):
    '''This class represents an existing Character Guide in the scene.'''

    
    def __init__(self, character_guide_name):
        '''
        @param character_guide_name: The name of an existing Character Guide.
        
        @see: To create a new Character Guide, see L{create_character_guide}.
        
        @raise CharacterGuideNotFoundError: see L{CharacterGuideNotFoundError}
        @raise NameNotCharacterGuideError: see L{NameNotCharacterGuideError}
        '''
        
        self.character_guide_name = character_guide_name

class CharacterGuideUtilities(object):
    '''A collection of utilities designed for the creation, deletion, and
    editing of a character guide.
    '''
    
    
    def __init__(self, character_guide_name):
        '''
        @param character_guide_name: The name of a Character Guide.
        '''
        
        self.character_guide_name = character_guide_name
    
    def create_character_guide(self):
        '''Create a character guide in the scene, and return the character guide
        object.
        
        @return: A L{CharacterGuide} object.
        '''
        pass
    
    def exists(self):
        '''Check if the character guide that this object represents, exists.
        @return: True if the Character Guide exists in the scene, false
        if it is either not in the scene, or not a properly formatted character
        guide.
        '''
        pass

class CharacterGuideNotFoundError(bcrf.bcrf_lib.exceptions.ObjectNotFound):
    '''A character guide was going to be loaded, but was not found.'''
    pass

class NameNotCharacterGuideError(bcrf.bcrf_lib.exceptions.ObjectTypeError):
    '''A name for a character guide was given, but it is either not a BCRF 
    Character Guide, or is not correctly formatted.'''
    pass

