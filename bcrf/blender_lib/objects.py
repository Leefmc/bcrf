'''An interface module to actions involving Blender Objects.'''

# standard
# related
# local


class Objects(object):
    '''A basic wrapper for common blender object oriented tasks.'''

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
