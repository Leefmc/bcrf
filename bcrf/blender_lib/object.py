'''An interface module to actions involving Blender Objects.'''

# standard
# related
# local


class FilterUtilities(object):
    '''A class with utilities for filtering sequences of objects and return a
    new filtered sequence.'''

    def __init__(self, *object_sequences):
        '''
        @param object_sequences: A tuple of all object_sequence arguments given
        to this function.
        
        @attention: Although this takes multiple sequences of objects as
        parameters, this, as with most of the framework, is not designed to
        handle multiple scenes at once.
        
        This is especially true if you give sequence(s) from SceneA and
        sequence(s) from SceneB to this class. Because this class combines
        the sequences
        '''
        
        objects = []
        for object_sequence in object_sequences:
            for object in object_sequence:
                objects.append(object)
        self.objects = tuple(objects)
    
    def endswith(self, endswith):
        '''Filter the sequences based on text that the object's names must end
        with.
        
        @todo: Code this.
        '''
        pass
    
    def contains(self, text):
        '''Return sequences that have the given text anywhere in their name.
        
        @todo: Code this.
        '''
        pass
    
    def selected(self):
        '''Return selected objects.
        
        @todo: Code this.
        '''
        pass
    
    def startswith(self, startswith):
        '''Filter the sequences based on text that the object's names must start
        with.
        
        @todo: Code this.
        '''
        pass
    
    def visible(self):
        '''Return visible objects.
        
        @todo: Code this.
        '''
        pass

class ObjectsUtilities(object):
    '''Utilities for a collection of Blender objects..'''

    def __init__(self, blender_objects):
        '''
        @param blender_objects: A Blender.Scene.SceneObjects class instance,
        containing a sequence of blender objects.
        '''
        self.blender_objects = blender_objects
    
    def exists(self, name):
        '''Check if an object exists in the scene.
        @param name: The name of the object to check the scene for.
        '''
        pass

class ObjectUtilities(object):
    '''Utilities for a Blender Object.'''

    def __init__(self, blender_object):
        '''
        @param blender_object: A Blender object instance.
        '''
        
        self.blender_object = blender_object

