'''This module provides code for creating and interacting with Character
Guides.'''

# standard
# related
import Blender.Scene
# local
import bcrf.blender_lib.scene
import bcrf.bcrf_lib.exceptions



class CharacterGuide(object):
    '''This class represents an existing Character Guide in the scene.'''

    
    def __init__(self, character_guide_name, scene=None):
        '''
        @param character_guide_name: The name of an existing Character Guide.
        @param scene: The scene that this class will use. If None, the
        L{bcrf.blender_lib.scene.Scene ActiveScene} is used.
        @type scene: A L{bcrf.blender_lib.scene.Scene} like object.
        
        @see: To create a new Character Guide, see L{create_character_guide}.
        
        @raise CharacterGuideNotFoundError: see L{CharacterGuideNotFoundError}
        @raise NameNotCharacterGuideError: see L{NameNotCharacterGuideError}
        '''
        
        if scene is None:
            self.scene = bcrf.blender_lib.scene.ActiveScene()
        else:
            self.scene = scene
        self.character_guide_name = character_guide_name
        
        self.character_utilities = CharacterGuideUtilities(
            character_guide_name, scene
        )
        
        # Create the switch functions
        def is_character_guide():
            pass
        
        def does_not_exist():
            raise CharacterGuideNotFoundError()
        
        def not_character_guide():
            raise NameNotCharacterGuideError()
        
        # Create the switch
        guide_existance_switch = {
            'is_character_guide':is_character_guide,
            'is_not_character_guide':not_character_guide,
            'object_does_not_exist':does_not_exist,
        }
        
        # Call switch
        guide_existance_switch[self.character_utilities.guide_state()]()

class CharacterGuideUtilities(object):
    '''A collection of utilities designed for the creation, deletion, and
    editing of a character guide.
    '''
    
    
    def __init__(self, character_guide_name, scene=None):
        '''
        @param character_guide_name: The name of a Character Guide.
        @param scene: The scene that this class will use. If None, the
        L{bcrf.blender_lib.scene.Scene ActiveScene} is used.
        @type scene: A L{bcrf.blender_lib.scene.Scene} like object.
        '''
        
        if scene is None:
            self.scene = bcrf.blender_lib.scene.ActiveScene()
        else:
            self.scene = scene
        self.character_guide_name = character_guide_name
    
    def create_character_guide(self):
        '''Create a character guide in the scene, and return the character guide
        object.
        
        @return: A L{CharacterGuide} object.
        '''
        pass
    
    def exists(self):
        '''Check if the character guide that this object represents, exists.
        @return: True if the Character Guide exists in the scene, False
        if it is either not in the scene, or not a properly formatted character
        guide.
        '''
        pass
    
    def get_character_guide(self):
        '''Return a character guide, by either creating or loading a
        character guide.
        
        @raise NameNotCharacterGuideError: see L{NameNotCharacterGuideError}
        '''
        
        # Load the character guide
        def is_character_guide():
            pass
        
        # Create the character guide
        def does_not_exist():
            pass
        
        # Raise an error.
        def not_character_guide():
            raise NameNotCharacterGuideError()
        
        # Create the switch
        guide_existance_switch = {
            'is_character_guide':is_character_guide,
            'is_not_character_guide':not_character_guide,
            'object_does_not_exist':does_not_exist,
        }
        
        # Call switch
        guide_existance_switch[self.guide_state()]()
    
    def guide_state(self):
        '''This function serves as a switch-able way of taking different
        actions based on the existance/formatting/whatever of the character
        guide. Instead of checking L{self.exists} and L{self.is_character_guide}
        this function can be used. The goal of it, is to summarize muiltiple
        states that the character guide can be in, and return a string based on
        those. This, inturn, can be used in a switch to create clean code paths.
        
        Note i am using strings, instead of integers, for readability.
        
        @return: Based on the status of this character guide, the following
        strings may be returned.
         - is_character_guide
         - is_not_character_guide
         - object_does_not_exist
        '''
        pass
    
    def is_character_guide(self):
        '''Check if the character guide that this object represents, is a
        valid character guide.
        @return: True if this is an _existing_ character guide, False if it
        does not exist or is not a properly formatted character guide.
        '''
        pass
    
    def load_character_guide(self):
        '''Load a Character Guide
        '''
        pass

class CharacterGuideNotFoundError(bcrf.bcrf_lib.exceptions.ObjectNotFound):
    '''A character guide was going to be loaded, but was not found.'''
    pass

class NameNotCharacterGuideError(bcrf.bcrf_lib.exceptions.ObjectTypeError):
    '''A name for a character guide was given, but it is either not a BCRF 
    Character Guide, or is not correctly formatted.'''
    pass

