'''This package contains packages of rig modules. Each Package is a descriptive
name for the type of rigging modules found within: generic or specific.

eg:
 - B{rig_modules.Arms.*}
   Arms would contain modules which will have specific attributes designed
   specifically for Arms. Generic modules are preferred over type specific
   modules such as these, but often some tasks are just done better if they
   have the ability to be specifically designed for a task. (In this case, arms)
   
 - B{rig_modules.two_segments.*}
   These are more generic. A module found in this category is designed to be
   _very_ generic. So generic, that using it for an arm, a leg, or even a door
   hinge, may all be possible.

@todo: Come up with a naming convention, and general design/layout scheme for
rig modules so that a user has an easy time finding the module they need.
'''

# standard
# related
# local


index = [
    'Arms'
]