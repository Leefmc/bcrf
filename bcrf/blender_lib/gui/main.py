''''''

# standard
# related
import Blender.Draw
# local
import bcrf.bcrf_lib.guide.character
import bcrf.blender_lib.object
import bcrf.blender_lib.scene
import bcrf.blender_lib.gui.base


class MainContainer(bcrf.blender_lib.gui.base.TabContainer):
    ''''''
    
    
    def draw(self):
        '''
        '''
        super(MainContainer, self).draw()

class GuideTabContent(bcrf.blender_lib.gui.base.TabContent):
    ''''''
    
    
    tab_header = 'Guide'
    button_title = 'GUIDE'
    
    def __init__(self, *args, **kw_args):
        '''Append the L{self._gui_event_switch}
        '''
        super(GuideTabContent, self).__init__(*args, **kw_args)
        
        # Append the true event id to the L{self._gui_event_switch}
        self._gui_event_switch[self._true_eid(1)] = self.build_guide_event
    
    def build_guide_event(self, event_id):
        '''This event is triggered when the "Build/Load" button is pressed.
        
        @attention: Since this is the only button at the moment, this is going
        to be a temporary testbed for direct framework calls.
        '''
        #cg_utils = bcrf.bcrf_lib.guide.character.CharacterGuideUtilities(
            #self._buttons['guide_name']
        #)
        #cg_utils.get_character_guide()
        
    
    def draw(self):
        '''
        '''
        super(GuideTabContent, self).draw()
        
        # Guide Name
        self._buttons['guide_name'] = Blender.Draw.String(
            'Guide Name: ',
            0,
            self.x, # X
            self.y + (self.height-20), # Y
            int(round(self.width*0.65)), 20, # Width, Height
            'bcrf_guide', # Default
            10, # Max Char Length
            'Enter the name for the Guide you want to Create or Load.'# Tooltip
        )
        
        # Create/Load
        Blender.Draw.PushButton(
            'Create/Load Guide', self._true_eid(1),
            int(self.x + self.width*0.65), # X + the width of the above string.
            self.y + (self.height-20), # Y
            int(round(self.width*0.35)), # Width
            20 # Height
        )

class RigTabContent(bcrf.blender_lib.gui.base.TabContent):
    ''''''
    
    
    tab_header = 'Rig'
    button_title = 'RIG'
    
    def __init__(self, *args, **kw_args):
        '''Initialize the L{self._gui_event_switch}
        '''
        super(RigTabContent, self).__init__(*args, **kw_args)
    
    def draw(self):
        '''
        '''
        super(RigTabContent, self).draw()
