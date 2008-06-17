'''A collection of base modules ment to be extended by user L{components}.'''

# standard
# related
# local


class Component(object):
    '''The base class for both rig and guide components.
    '''

    def __init__(self, base_name):
        '''
        @param base_name: The base name of the component. This will be used
        in much of the naming conventions.
        '''
        self.base_name = base_name

class GuideComponent(Component):
    '''The base for guide components.
    '''

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
        
        @important: Keep in mind that the last object in the sequence will
        not have tracking applied to it, because there must be an object
        for the "tracker" to point to.
        
        @raise SomeException: Raised if there is only one object given to the
        rotation object. There needs to be atleast 2 object given to this
        function.
        
        @todo: Replace the fake exception with a real one.. heh.
        '''
        
        if len(objects) < 2:
            raise Exception('REPLACE ME WITH A REAL EXCEPTION')

class RigComponent(Component):
    '''The base for rig components.
    '''

