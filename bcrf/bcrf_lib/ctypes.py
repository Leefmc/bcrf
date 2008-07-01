'''This module holds constants used to identify BCRF Types.'''

# standard
import exceptions
# related
# local
import bcrf.ctypes


class BCRFType(bcrf.ctypes.CustomType):
    '''The base BCRF type.
    '''
    pass

class Character(BCRFType):
    '''
    '''
    pass

class CharacterGuide(Character):
    '''A Blender Object that is compatible with
    L{bcrf.bcrf_lib.guide.character.CharacterGuide}.'''
    pass

class CharacterRig(Character):
    '''
    '''
    pass

class Component(BCRFType):
    '''
    '''
    pass

class ComponentGuide(Component):
    '''
    '''
    pass

class ComponentRig(Component):
    '''
    '''
    pass

class Data(BCRFType):
    '''This type is intended to strictly store data. Any object can store
    data, but by using a specific object type for this, finding data can be
    semi-standardized.
    '''
    pass
