'''Basic exceptions for BCRF.'''

# standard
# related
# local


class BCRFError(Exception):
    '''The base BCRF exception.'''
    pass

class ObjectNotFound(BCRFError):
    '''An object was being accessed, but was not found.'''
    pass

class ObjectTypeError(BCRFError):
    '''An object, I{Blender or BCRF}, of a specific type was expected but the
    object given is not of that type.'''
    pass

class ReservedBCRFString(BCRFError):
    '''A value was given to something that has the ability to store a
    "bcrf type", but the value was the same as a bcrf type. Often this is a
    string value given, I{such as "bcrftTrue"}.'''
    pass
