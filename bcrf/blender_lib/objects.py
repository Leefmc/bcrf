'''An interface module to actions involving Blender Objects.'''

# standard
# related
# local


class ObjectsUtilities(object):
    '''A basic wrapper for common blender object oriented utilities.'''

    def __init__(self, blender_objects):
        '''
        @param blender_objects: A Blender.Scene.SceneObjects class, containing a
        collection of blender objects.
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
        '''
        
        
    
    