'''An interface module to actions involving Blender Scenes.'''

# standard
# related
import Blender.Scene
# local
import bcrf.blender_lib.object
import bcrf.blender_lib.ctypes


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
        @return: A BCRF object collection for all the objects in the scene.
        @rtype: L{bcrf.blender_lib.object.ObjectCollection}
        '''
        return bcrf.blender_lib.object.Object(self.blender_scene.active)
    
    def all_objects(self):
        '''
        @return: A BCRF object collection for all the objects in the scene.
        @rtype: L{bcrf.blender_lib.object.ObjectCollection}
        '''
        return bcrf.blender_lib.object.ObjectCollection(
            self.blender_scene.objects)
    
    def create_object(self, bcrf_type, name='BCRFObject'):
        '''This creates an object and assigns some basic standardized data to
        it; Such as, the BCRF Type.
        @param bcrf_type: A basic, standalone,
        L{bcrf.blender_lib.ctypes BCRF Type}.
        @param name: The objects name.
        '''
        blender_object = self.blender_scene.objects.new(
            bcrf_type.blender_creation_data())
        object = bcrf.blender_lib.object.Object(blender_object)
        blender_object.name = name
        
        object.data['bcrf_type'] = bcrf_type.bcrf_type()
        
        return object
    
    def selected_objects(self, only_visible=True):
        '''
        @param only_visible: If True, only the visible selected objects
        in the scene are returned.
        
        @return: A BCRF object collection for all the objects in the scene.
        @rtype: L{bcrf.blender_lib.object.ObjectCollection}
        '''
        if only_visible:
            return bcrf.blender_lib.object.ObjectCollection(
                self.blender_scene.selected)
        else:
            return bcrf.blender_lib.object.ObjectCollection(
                self.blender_scene.context)

class ActiveScene(Scene):
    '''A wrapper for the Active Blender Scene.'''
    
    
    def __init__(self):
        '''
        '''
        super(ActiveScene, self).__init__(Blender.Scene.GetCurrent())

