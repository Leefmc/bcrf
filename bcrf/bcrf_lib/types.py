'''This module holds constants used to identify BCRF Types.'''

# standard
# related
# local

'''A Blender Object.
This basically means that it is not a BCRF object, and for further information
on what this object is, look it up to see what L{bcrf.blender_lib.types Type}
it is.'''
BLENDER = 'bcrf.bcrf_lib.types.BLENDER'

'''A Blender Object that is compatible with
L{bcrf.bcrf_lib.guide.character.CharacterGuide}.'''
CHARACTER_GUIDE = 'bcrf.bcrf_lib.types.CHARACTER_GUIDE'

CHARACTER_RIG = 'bcrf.bcrf_lib.types.CHARACTER_RIG'

'''A Blender Object that is part of, and possibly compatible with, a 
L{bcrf.bcrf_lib.guide.component.ComponentGuide}.'''
COMPONENT_GUIDE = 'bcrf.bcrf_lib.types.COMPONENT_GUIDE'

'''A Blender Object that is part of, and possibly compatible with, a 
L{bcrf.bcrf_lib.rig.component.ComponentRig}.'''
COMPONENT_RIG = 'bcrf.bcrf_lib.types.COMPONENT_RIG'
