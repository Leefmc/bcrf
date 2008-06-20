'''Basic exceptions for rig_lib.'''

# standard
# related
# local


class BCRFRigLibError(Exception):
    '''The base BCRF rig_lib exception.'''
    pass

class ObjectNotFound(BCRFRigLibError):
    '''An object was being accessed, but was not found.'''
    pass

class ObjectTypeError(BCRFRigLibError):
    '''An object, I{Blender or BCRF}, of a specific type was expected but the
    object given is not of that type.'''
    pass
