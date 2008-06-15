'''An interface module to actions involving Blender Scenes.'''

# standard
# related
import Blender.Scene
# local
import bcrf.blender_lib.objects


class Scene(object):
    '''A wrapper for a Blender Scene.'''

    def __init__(self, blender_scene):
        '''
        @param blender_scene: A Blender Scene.
        '''
        self.blender_scene = blender_scene
    
    def all_objects(self):
        '''
        @return: A BCRF Wrapper for all the objects in the scene.
        @rtype: L{bcrf.blender_lib.objects.Objects}
        '''
        return bcrf.blender_lib.objects.Objects(
            self.blender_scene.objects
        )
    
    def selected_objects(self, only_visible=True):
        '''
        @param only_visible: If True, only the visible selected objects
        in the scene are returned.
        
        @return: A BCRF Wrapper for all the selected objects in the scene.
        @rtype: L{bcrf.blender_lib.objects.Objects}
        '''
        return bcrf.blender_lib.objects.Objects(
            self.blender_scene.objects
        )

class ActiveScene(Scene):
    '''A wrapper for the Active Blender Scene.'''
    
    def __init__(self):
        '''
        '''
        super(ActiveScene, self).__init__(Blender.Scene.GetCurrent())
