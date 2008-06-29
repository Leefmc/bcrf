'''The base types.. though there basically are none. bcrf, and blender,
are very different in practice. This module is mainly here because of the need
for a common type base class, L{CustomType}.'''

# standard
import exceptions
# related
# local
import bcrf.bcrf_lib.ctypes
import bcrf.blender_lib.ctypes


def get_type(object):
    '''
    @param object: A L{bcrf.blender_lib.object.Object} like object.
    
    @return: The L{CustomType} class for the type of object. If the object
    does not match any supported types, None is returned.
    '''
    bcrf_path = 'bcrf.bcrf_lib.ctypes.'
    blender_path = 'bcrf.blender_lib.ctypes.'
    type_dict = {
        '%sCharacterGuide' % bcrf_path:bcrf.bcrf_lib.ctypes.CharacterGuide,
        '%sCharacterRig' % bcrf_path:bcrf.bcrf_lib.ctypes.CharacterRig,
        '%sComponentGuide' % bcrf_path:bcrf.bcrf_lib.ctypes.ComponentGuide,
        '%sComponentRig' % bcrf_path:bcrf.bcrf_lib.ctypes.ComponentRig,
        
        '%sCurve' % blender_path:bcrf.blender_lib.ctypes.Curve,
        '%sEmpty' % blender_path:bcrf.blender_lib.ctypes.Empty,
        '%sMesh' % blender_path:bcrf.blender_lib.ctypes.Mesh,
    }
    
    stored_bcrf_type = object.stored_bcrf_type()
    if type_dict.has_key(stored_bcrf_type):
        return type_dict[stored_bcrf_type]
    else:
        return None

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
    def creation_data(self):
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
