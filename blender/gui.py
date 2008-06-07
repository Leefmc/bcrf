'''The main gui interface to users inside of blender.'''

# standard
# related
import Blender
# local

class MainGUI(object):
    ''''''

    # 1000 series = Generic UI Elements (close, about, help, etc)
    EVT_CLOSEGUI_BTN = 1001
    EVT_ABOUT_BTN = 1002
    EVT_HELP_BTN = 1003
    
    # Each Tab has its own series so content can use the same series.
    EVT_GUIDE_TAB = 1100
    EVT_RIG_TAB = 1200
    EVT_XML_TAB = 1300
    
    gui_width = 500
    gui_height = 400
    
    def __init__(self):
        '''Constructor
        '''
        pass
    
    def _events(self, event_id):
        '''
        '''
        def not_handled():
            '''A simple function to use for events that
            are not handled.'''
            pass
        
        # Define the python switch for the event ID
        event_switch = {
            self.EVT_CLOSEGUI_BTN:self.closegui_btn_clicked_event,
            self.EVT_ABOUT_BTN:self.about_btn_clicked_event,
            self.EVT_HELP_BTN:not_handled,
            
            self.EVT_GUIDE_TAB:self.guide_tab_clicked_event,
            self.EVT_RIG_TAB:not_handled,
            self.EVT_XML_TAB:not_handled,
        }
        # Call the switch
        event_switch[event_id]()
    
    def _gui(self):
        '''
        '''
        # A dict of the box edge coordinates
        edge_locs = {
            'left':3,
            'right':0,
            'top':0,
            'bottom':3
        }
        
        button_height = 20
        button_width = 100
        
        # Draw the buttons. Drawn in the order of the Event ID'S
        Blender.Draw.PushButton(
            'CloseGUI', self.EVT_CLOSEGUI_BTN,
            edge_locs['left'],
            edge_locs['bottom'], button_width, button_height)
        Blender.Draw.PushButton(
            'About', self.EVT_ABOUT_BTN,
            button_width * 1 + edge_locs['left'],
            edge_locs['bottom'], button_width, button_height)
        Blender.Draw.PushButton(
            'Help', self.EVT_HELP_BTN,
            button_width * 2 + edge_locs['left'],
            edge_locs['bottom'], button_width, button_height)
        
        tab_width = self.gui_width/3
        Blender.Draw.PushButton(
            'GUIDE', self.EVT_GUIDE_TAB,
            edge_locs['left'] + (tab_width*0),
            20 + edge_locs['bottom'],
            tab_width, button_height)
        Blender.Draw.PushButton(
            'RIG', self.EVT_GUIDE_TAB,
            edge_locs['left'] + (tab_width*1),
            20 + edge_locs['bottom'],
            tab_width, button_height)
        Blender.Draw.PushButton(
            'XML', self.EVT_GUIDE_TAB,
            edge_locs['left'] + (tab_width*2),
            20 + edge_locs['bottom'],
            tab_width, button_height)
    
    def about_btn_clicked_event(self):
        '''Display the About Dialog.
        '''
        home_url = Blender.Draw.Create(
            'http://code.google.com/p/bmrf/')
        source_url = Blender.Draw.Create(
            'http://github.com/Leefmc/bmrf')
        
        block = [
            'Home: ',
            (
                '', 
                home_url, 0, 30, '',
                ),
            'Source: ',
            (
                '', 
                source_url, 0, 30, '',
                ),
            '',
            'Special Credits to:',
            'The Blender Foundation',
        ]

        Blender.Draw.PupBlock('About BMRF', block)
    
    def closegui_btn_clicked_event(self):
        '''Execute any saving prefs code, then Close the GUI.
        '''
        Blender.Draw.Exit()
    
    def display(self):
        '''Display the GUI.
        '''
        Blender.Draw.Register(self._gui, None, self._events)
    
    def guide_tab_clicked_event(self):
        '''Display the Guide Tab.
        '''
        print 'guide-tab-clicked'
    
    def xml_tab_clicked_event(self):
        '''Display the XML Tab.
        '''
        pass
    

# Create the GUI instance
main_gui = MainGUI()

# Display the GUI
main_gui.display()

