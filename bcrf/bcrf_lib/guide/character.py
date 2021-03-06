'''This module provides code for creating and interacting with Character
Guides.'''

# standard
import exceptions
# related
import Blender.Scene
# local
import bcrf.bcrf_lib.errors
import bcrf.bcrf_lib.ctypes
import bcrf.blender_lib.object
import bcrf.blender_lib.scene


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
        
        @todo: Add object data to it, to create the actual "Character Guide"
        base.
        '''
        # Create the blender object for the character guide.
        object = self.scene.create_object(
            bcrf.bcrf_lib.ctypes.CharacterGuide,
            name=self.character_guide_name
        )
        
        # Add data to that object, so that bcrf knows its a bcrf object.
        cg_data = CharacterGuideData(object)
        
        return CharacterGuide(self.character_guide_name)
    
    def exists(self):
        '''Check if the character guide that this object represents, exists.
        @return: True if the Character Guide exists in the scene, False
        if it is either not in the scene, or not a properly formatted character
        guide.
        '''
        raise exceptions.NotImplementedError()
    
    def get_character_guide(self):
        '''Return a character guide, by either creating or loading a
        character guide.
        
        @raise NameNotCharacterGuideError: see L{NameNotCharacterGuideError}
        
        @todo: The L{self.guide_state guide_state} method is soon to be removed,
        so the methodology needs to be replaced here. It will be replaced
        with a simple try/except method, initialized by creating the character
        guide itself.
        '''
        
        # Load the character guide
        def is_character_guide():
            return CharacterGuide(self.character_guide_name, self.scene)
        
        # Create the character guide
        def does_not_exist():
            return self.create_character_guide()
        
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
        
        @deprecated: This method will be removed soon because it.. stinks.
        '''
        # Get the scene objects
        all_blender_objects = self.scene.all_objects()
        # Check if the character guide name is in the collection, if not it
        # does not exist.
        if not all_blender_objects.has_key(self.character_guide_name):
            return 'object_does_not_exist'
        
        # The is comparison may not be correct here.
        if self.is_character_guide():
            return 'is_character_guide'
        else:
            return 'is_not_character_guide'
        
    
    def is_character_guide(self):
        '''Check if the character guide that this object represents, is a
        valid character guide.
        @return: True if this is an _existing_ character guide, False if it
        does not exist or is not a properly formatted character guide.
        '''
        # Get the scene objects
        all_objects = self.scene.all_objects()
        
        object_to_inspect = all_objects[
            self.character_guide_name]
        return bcrf.bcrf_lib.ctypes.CharacterGuide.check_object_type(
            object_to_inspect)
    
    def load_character_guide(self):
        '''Load a Character Guide
        '''
        raise exceptions.NotImplementedError()

class CharacterGuideData(object):
    '''An interface to an objects data, limited to the keys of a Character
    Guide.
    
    @attention: Remember, this is just an interface to an objects data,
    the interface itself has been limited to Character Guide data. This means
    that at no point does it enforce that all the data in the object, pertains
    to I{only} the character guide, but rather it only reads and writes data
    pertaining to a character guide.
    
    @todo: Currently all properties try to use an object of self._propertyname,
    this is obviously incorrect. It is simply written that way because that is
    my default WingIDE Template. Because of this, all properties need to be
    re-written internally to support ObjectData['propname'].
    '''

    def __init__(self, object):
        '''
        @param object: An instance of an L{bcrf.blender_lib.object.Object}
        '''
        
        self.object = object
        self.object_data = bcrf.blender_lib.object.ObjectDataDict(object)
    
    def _property_get_name(self):
        return self.object_data['name']
    
    def _property_set_name(self, value):
        self.object_data['name'] = value
    
    name = property(
        _property_get_name,
        _property_set_name,
    )
    
    def _property_get_type(self):
        return self.object_data['type']
    
    def _property_set_type(self, value):
        self.object_data['type'] = value
    
    type = property(
        _property_get_type,
        _property_set_type,
    )
    

class CharacterGuideNotFoundError(bcrf.bcrf_lib.errors.ObjectNotFound):
    '''A character guide was going to be loaded, but was not found.'''
    pass

class NameNotCharacterGuideError(bcrf.bcrf_lib.errors.ObjectTypeError):
    '''A name for a character guide was given, but it is either not a BCRF 
    Character Guide, or is not correctly formatted.'''
    pass

