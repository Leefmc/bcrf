'''Base classes for classes for many sub-modules & packages.'''

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
