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
    
    
    # Generic Dimensions.
    ## Keep in mind changes to these may impact more than you'd expect,
    ## so be aware of what you're changing.
    # A dict of the box edge coordinates, from the bottom-left up.
    gui_border_locations = {
        'left':3, # Left border at X:3pix
        'right':400, # Right border at X:400px
        'bottom':3, # Bottom border at Y:3pix
        'top':500, # Top border at Y:0px
    }
    # Gui dimensions calculated from above.
    gui_width = gui_border_locations['right'] - gui_border_locations['left']
    gui_height = gui_border_locations['top'] - gui_border_locations['bottom']
    
    '''The tab that will be rendered, when L{self._gui} is called.'''
    current_tab = 'guide'
    
    
    def __init__(self):
        '''Constructor
        '''
        pass
    
    def _draw_guide_tab_gui(self):
        '''Draw the GUI for the guide tab's contents.
        
        @attention: Make sure only drawing code is within the drawing functions.
        Blender seems to initialize the drawing function (L{self._gui}) many
        times in one session, possibly whenever blender/this gui loses focus.
        '''
        pass
    
    def _draw_rig_tab_gui(self):
        '''Draw the GUI for the rig tab's contents.
        
        @attention: Make sure only drawing code is within the drawing functions.
        Blender seems to initialize the drawing function (L{self._gui}) many
        times in one session, possibly whenever blender/this gui loses focus.
        '''
        pass
    
    def _draw_stateless_gui(self):
        '''Draw the stateless gui. ie, the one which is on every tab state.
        
        @attention: Make sure only drawing code is within the drawing functions.
        Blender seems to initialize the drawing function (L{self._gui}) many
        times in one session, possibly whenever blender/this gui loses focus.
        '''
        button_height = 20
        button_width = 100
        
        # Draw the buttons. Drawn in the order of the Event ID'S
        Blender.Draw.PushButton(
            'CloseGUI', self.EVT_CLOSEGUI_BTN,
            self.gui_border_locations['left'],
            self.gui_border_locations['bottom'], button_width, button_height)
        Blender.Draw.PushButton(
            'About', self.EVT_ABOUT_BTN,
            button_width * 1 + self.gui_border_locations['left'],
            self.gui_border_locations['bottom'], button_width, button_height)
        Blender.Draw.PushButton(
            'Help', self.EVT_HELP_BTN,
            button_width * 2 + self.gui_border_locations['left'],
            self.gui_border_locations['bottom'], button_width, button_height)
        
        tab_width = self.gui_width/3
        Blender.Draw.PushButton(
            'GUIDE', self.EVT_GUIDE_TAB,
            self.gui_border_locations['left'] + (tab_width*0),
            20 + self.gui_border_locations['bottom'],
            tab_width, button_height)
        Blender.Draw.PushButton(
            'RIG', self.EVT_RIG_TAB,
            self.gui_border_locations['left'] + (tab_width*1),
            20 + self.gui_border_locations['bottom'],
            tab_width, button_height)
        Blender.Draw.PushButton(
            'XML', self.EVT_XML_TAB,
            self.gui_border_locations['left'] + (tab_width*2),
            20 + self.gui_border_locations['bottom'],
            tab_width, button_height)
    
    def _draw_xml_tab_gui(self):
        '''Draw the GUI for the xml tab's contents.
        
        @attention: Make sure only drawing code is within the drawing functions.
        Blender seems to initialize the drawing function (L{self._gui}) many
        times in one session, possibly whenever blender/this gui loses focus.
        '''
        pass
    
    ## Defined after the _draw's so it can reference them.
    # Draw Tab Switch, responsible for calling the draw functions for each tab.
    draw_tab_switch = {
        'guide':_draw_guide_tab_gui,
        'rig':_draw_rig_tab_gui,
        'xml':_draw_xml_tab_gui,
    }
    
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
            self.EVT_RIG_TAB:self.rig_tab_clicked_event,
            self.EVT_XML_TAB:self.xml_tab_clicked_event,
        }
        # Call the switch
        event_switch[event_id]()
    
    def _gui(self):
        ''' Actually draw the GUIs, and decide which GUIs to draw.
        '''
        # Draw the stateless
        self._draw_stateless_gui()
        # Draw the current tab.
        self.draw_tab_switch[self.current_tab](self)
    
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
        '''Display the GUI for the first time.
        '''
        # Currently, there is no difference in the first state and a redraw
        # since all values have defaults. So simply call redraw.
        self.redraw_display()
    
    def guide_tab_clicked_event(self):
        '''Display the Guide Tab.
        '''
        if self.current_tab != 'guide':
            self.current_tab = 'guide'
            self.redraw_display()
    
    def redraw_display(self):
        '''Redraw the display GUI.
        '''
        Blender.Draw.Register(self._gui, None, self._events)
    
    def rig_tab_clicked_event(self):
        '''Display the Rig Tab.
        '''
        if self.current_tab != 'rig':
            self.current_tab = 'rig'
            self.redraw_display()
    
    def xml_tab_clicked_event(self):
        '''Display the XML Tab.
        '''
        if self.current_tab != 'xml':
            self.current_tab = 'xml'
            self.redraw_display()
    

# Create the GUI instance
main_gui = MainGUI()

# Display the GUI
main_gui.display()

