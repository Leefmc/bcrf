'''An interface module to actions involving Blender Scenes.'''

# standard
# related
import Blender.Scene
# local
import bcrf.blender_lib.object


class Scene(object):
    '''A wrapper for a Blender Scene. This provides only generic functions with
    basic scene classes automatically initialized.
    '''
    

    def __init__(self, blender_scene):
        '''
        @param blender_scene: A Blender Scene.
        '''
        self.blender_scene = blender_scene
    
    def active_object(self):
        '''
        @return: A BCRF utilities object for all the objects in the scene.
        @rtype: L{bcrf.blender_lib.object.ObjectsUtilities}
        '''
        return self.blender_scene.active
    
    def all_objects(self):
        '''
        @return: A tuple of all objects.
        '''
        return tuple(self.blender_scene.objects)
    
    def selected_objects(self, only_visible=True):
        '''
        @param only_visible: If True, only the visible selected objects
        in the scene are returned.
        
        @return: A tuple of selected objects.
        '''
        if only_visible:
            return tuple(self.blender_scene.selected)
        else:
            return tuple(self.blender_scene.context)

class ActiveScene(Scene):
    '''A wrapper for the Active Blender Scene.'''
    
    
    def __init__(self):
        '''
        '''
        super(ActiveScene, self).__init__(Blender.Scene.GetCurrent())

