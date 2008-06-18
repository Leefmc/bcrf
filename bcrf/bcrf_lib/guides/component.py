'''A collection of code involving component guides'''

# standard
# related
# local
import bcrf.bcrf_lib.base


class GuideComponent(bcrf.bcrf_lib.base.Component):
    '''The base for guide components.
    
    @todo: Move the "tool" like functions into a different location in
    the framework.
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