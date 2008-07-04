'''The base types.. though there basically are none. bcrf, and blender,
are very different in practice. This module is mainly here because of the need
for a common type base class, L{CustomType}.'''

# standard
import exceptions
# related
# local


def get_type(object):
    '''
    @deprecated: See L{bcrf.blender_lib.object.Object.type}
    '''
    pass

class CustomType(object):
    '''The base type for the L{bcrf.bcrf_lib bcrf_lib} and
    L{bcrf.blender_lib blender_lib} libraries.
    
    Because BCRF has to essentially define its own types for Blender objects,
    it simply assigns a "bcrf_type" property with each object it needs, and
    a string is stored there. This string represents a type, such as those
    found here.
    If the string is not found, it is assumed to be a standard Blender object.
    '''
    
    def __init__(self):
        '''This init is simply here to fail (Boy that sounds harsh), because
        classes that inherit from CustomType are not expected to be instances.
        '''
        return exceptions.NotImplementedError(
            'Instances of CustomType are not supported.'
        )
    
    @classmethod
    def bcrf_type(cls):
        '''
        @return: This returns the full module path and class name. The purpose
        of this is so that each class has a unique type name.
        '''
        return '%s.%s' % (str(cls.__module__), str(cls.__name__),)
    
    @classmethod
    def check_object_type(cls, object):
        '''Check if a blender object is of the same type as this class.
        @param object: A L{bcrf.blender_lib.object.Object} like object.
        @return: True of False, depending if the blender object given is of
        this class type or not.
        '''
        return object.type() is cls
    
    @classmethod
    def blender_creation_data(cls):
        '''When creating a new Blender, the BPY API takes a data object
        for the new object you are going to create. This function returns an
        instance of that data type.
        
        Keep in mind that multiple BCRF Types may actually share the same
        data type, because in Blender they are the same object. So the
        blender data object is not a unique representation of the BCRF type in
        any way.
        
        @return: Default to an Empty.
        '''
        return 'Empty'
