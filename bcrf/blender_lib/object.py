'''An interface module to actions involving Blender Objects.'''

# standard
import exceptions
# related
# local
import bcrf.ctypes
import bcrf.bcrf_lib.ctypes
import bcrf.bcrf_lib.errors
import bcrf.blender_lib.ctypes



class Object(object):
    '''A wrapper for a single Blender Object.'''

    def __init__(self, blender_object):
        '''
        @param blender_object: A Blender object instance.
        '''

        self.blender_object = blender_object
        self.data = ObjectDataDict(self)

    def type():
        '''
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

class ObjectCollection(dict):
    '''A wrapper for a collection of Blender objects.'''

    def __init__(self, blender_object_collection):
        '''
        @param blender_objects_collection: A Blender.Scene.SceneObjects
        class instance.

        @attention: Although this takes multiple collections of objects as
        parameters, this, as with most of the framework, is not designed to
        handle multiple scenes at once.

        This is especially true if you give sequence(s) from SceneA and
        sequence(s) from SceneB to this class. Because this class combines
        the collections. It may work, or it may fail horribly. It has not, and
        will not, be handled.
        '''
        for blender_object in blender_object_collection:
            object_name = blender_object.getName()
            if self.has_key(object_name):
                raise exceptions.KeyError(
                    'The key "'+object_name+'" already exists '
                    'in this ObjectCollection.'
                )
            self[object_name] = blender_object

    def exists(self, name):
        '''Check if an object exists in the scene.
        @param name: The name of the object to check the scene for.
        '''
        pass

    def filter_endswith(self, endswith):
        '''Filter the sequences based on text that the object's names must end
        with.

        @todo: Code this.
        '''
        pass

    def filter_contains(self, text):
        '''Return sequences that have the given text anywhere in their name.

        @todo: Code this.
        '''
        pass

    def filter_selected(self):
        '''Return selected objects.

        @todo: Code this.
        '''
        pass

    def filter_startswith(self, startswith):
        '''Filter the sequences based on text that the object's names must start
        with.

        @todo: Code this.
        '''
        pass

    def filter_visible(self):
        '''Return visible objects.

        @todo: Code this.
        '''
        pass

class ObjectDataDict(dict):
    '''A wrapper for writing/reading object data stored in Blender's
    "ID Properties". The purpose of this wrapper is mainly to allow extra data
    type storage. Simple things such as Booleans are implemented by storing
    strings like "bcrfTrue", then interpreting them during a read/write.
    '''


    _bcrf_read_types = {
        'bcrftTrue':True,
        'bcrftFalse':False,
        'bcrftNone':None,
    }

    _bcrf_write_types = {
        True:'bcrftTrue',
        False:'bcrftFalse',
        None:'bcrftNone',
    }

    def __init__(self, object):
        '''
        @param object: The object this class will use to store data in.
        @type object: A L{Object} like object.
        '''

        self.object = object
        self.blender_object_properties = object.blender_object.properties

    def __getitem__(self, key):
        '''
        '''
        # Pull the data from the Blender Object
        blender_value = self.blender_object_properties[key]

        # Check if the value is a bcrf type.
        # If it is, return the value replacement.
        if self._bcrf_read_types.has_key(blender_value):
            return self._bcrf_read_types[key]
        # Yes i know, this else is not needed. Its easier to read though!
        # If it is not, return the actual value.
        else:
            return blender_value

    def __len__(self):
        '''
        '''
        return len(self.blender_object_properties)

    def __setitem__(self, key, value):
        '''
        @raise bcrf.bcrf_lib.errors.ReservedBCRFString: See
        L{bcrf.bcrf_lib.errors.ReservedBCRFString ReservedBCRFString}
        '''
        print 'Assigning Object Data:\n\tKey:%s\n\tValue:%s\n\tObject Name:%s\n' % (
            key,
            value,
            self.object.blender_object.name,
        )
        # If the value matches a string that is considered a "bcrf type",
        # raise an exception because the value will write, but upon reading
        # it will be replaced with the type that the bcrf type represents.
        if self._bcrf_read_types.has_key(value):
            raise bcrf.bcrf_lib.errors.ReservedBCRFString(
                '''The value I{%s} is a reserved BCRF Type, representing the
                true value I{%s}''' % (value, self._bcrf_read_types[value])
            )
        # Check if the value is a bcrf type.
        # If it is, set the value replacement.
        elif self._bcrf_write_types.has_key(value):
            self.blender_object_properties[key] = self._bcrf_write_types[value]
        # If it is not, set the actual value.
        else:
            self.blender_object_properties[key] = value

    def __str__(self):
        '''
        '''
        return str(self.blender_object_properties)

