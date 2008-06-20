'''A collection of code involving component guides'''

# standard
import exceptions
# related
# local
import bcrf.bcrf_lib.base


class ComponentGuideUtilities(object):
    '''A collection of utilities designed for the creation, deletion, and
    editing of a component guide.
    '''

    
    def __init__(self, component_base_name):
        '''
        @param component_base_name: The base name of the component that these
        utilities will be focused on.
        '''
        self.component_base_name = component_base_name
    
    def add_translate_guide(name, position=(0,0,0), rotation=(0,0,0), scale=1):
        '''
        '''
        pass

    def add_rotation_trackers(objects):
        '''This function allows translate only guides to have rotations
        caluclated. Rotation is figured by a hidden object under the translate
        object having a directional constraint applied to it, pointing to the
        next object in the series.
        
        @param objects: An sequence of bcrf objects that will be used to create
        the trackers. Each object will be used to create, in order,
        rotation trackers at their positions.
        
        @note: Keep in mind that the last object in the sequence will
        not have tracking applied to it, because there must be an object
        for the "tracker" to point to.
        
        @raise ValueError: Raised if there is only one object given to the
        rotation object. There needs to be atleast 2 object given to this
        function.
        '''
        
        if len(objects) < 2:
            raise exceptions.ValueError('The objects argument must have 2 or '
            'more objects within.')

class ComponentGuide(bcrf.bcrf_lib.base.Component):
    '''The base for guide components.
    '''

