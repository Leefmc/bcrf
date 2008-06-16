'''The main gui interface to users inside of blender.'''

# standard
# related
import Blender
# local
import bcrf.bcrf_lib


class MainGUI(object):
    ''''''

    # 1000 series = Generic UI Elements (close, about, help, etc)
    EVT_CLOSEGUI_BTN = 1001
    EVT_ABOUT_BTN = 1002
    EVT_HELP_BTN = 1003
    
    # Each Tab has its own series so content can use the same series.
    EVT_GUIDERIG_TAB = 1100
    EVT_COMPTEST_TAB = 1200
    EVT_XML_TAB = 1300
    EVT_COMPONENTS_TAB = 1400
    EVT_MENU_TAB = 1500
    
    # GuideTab Content
    EVT_GUIDERIGTAB_GNAME = 1101
    EVT_GUIDERIGTAB_CREATE = 1102
    
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
    # Gui dimensions calculated from the above border positions.
    gui_width = gui_border_locations['right'] - gui_border_locations['left']
    gui_height = gui_border_locations['top'] - gui_border_locations['bottom']
    
    '''The tab that will be rendered, when L{self._gui} is called.'''
    current_tab = 'guiderig'
    
    
    def __init__(self):
        '''Constructor
        '''
    
    def _draw_guiderig_tab_gui(self):
        '''Draw the GUI for the guide/rig tab's contents.
        
        @attention: Make sure only drawing code is within the drawing functions.
        Blender seems to initialize the drawing function (L{self._gui}) many
        times in one session, possibly whenever blender/this gui loses focus.
        '''
        # Tab Name
        Blender.Draw.Label(
            'TAB: GUIDE RIG',
            self.gui_border_locations['left'], # X, y, w, h)
            self.gui_border_locations['top'] - 20, # Y - LabelHeight
            self.gui_width, # Width
            20 # Height
        )
        
        # Guide Name
        Blender.Draw.String(
            'Guide Name: ', self.EVT_GUIDERIGTAB_GNAME,
            self.gui_border_locations['left'], # X
            self.gui_border_locations['top'] - 40, # Y - Height+TabName
            int(self.gui_width*0.65), 20, # Width, Height
            'bcrf_guide', # Default
            25, # Max Char Length
            'Enter the name for the Guide you want to Create or Load.'# Tooltip
        )
        
        # Create/Load
        Blender.Draw.PushButton(
            'Create/Load Guide', self.EVT_GUIDERIGTAB_CREATE,
            int(self.gui_border_locations['left'] + self.gui_width*0.65), # X
            self.gui_border_locations['top'] - 40, # Y
            int(self.gui_width*0.35), # Width
            20 # Height
        )
    
    def _draw_components_tab_gui(self):
        '''Draw the GUI for the compoent tab's contents.
        
        @attention: Make sure only drawing code is within the drawing functions.
        Blender seems to initialize the drawing function (L{self._gui}) many
        times in one session, possibly whenever blender/this gui loses focus.
        '''
        
        # Tab Name
        Blender.Draw.Label(
            'TAB: COMPONENTS',
            self.gui_border_locations['left'], # X, y, w, h)
            self.gui_border_locations['top'] - 20, # Y - LabelHeight
            self.gui_width, # Width
            20 # Height
        )
    
    def _draw_menu_tab_gui(self):
        '''Draw the GUI for the menu tab's contents.
        
        @attention: Make sure only drawing code is within the drawing functions.
        Blender seems to initialize the drawing function (L{self._gui}) many
        times in one session, possibly whenever blender/this gui loses focus.
        '''
        
        # Tab Name
        Blender.Draw.Label(
            'TAB: MENU',
            self.gui_border_locations['left'], # X, y, w, h)
            self.gui_border_locations['top'] - 20, # Y - LabelHeight
            self.gui_width, # Width
            20 # Height
        )
    
    def _draw_comptest_tab_gui(self):
        '''Draw the GUI for the comptest tab's contents.
        
        @attention: Make sure only drawing code is within the drawing functions.
        Blender seems to initialize the drawing function (L{self._gui}) many
        times in one session, possibly whenever blender/this gui loses focus.
        '''
        
        # Tab Name
        Blender.Draw.Label(
            'TAB: COMPONENT TESTING',
            self.gui_border_locations['left'], # X, y, w, h)
            self.gui_border_locations['top'] - 20, # Y - LabelHeight
            self.gui_width, # Width
            20 # Height
        )
    
    def _draw_stateless_gui(self):
        '''Draw the stateless gui. ie, the one which is on every tab state.
        
        @attention: Make sure only drawing code is within the drawing functions.
        Blender seems to initialize the drawing function (L{self._gui}) many
        times in one session, possibly whenever blender/this gui loses focus.
        '''
        button_height = 20
        button_width = 75
        
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
        
        tab_height = 15
        tab_width = self.gui_width/5
        tab_ypos = 22 + self.gui_border_locations['bottom']
        Blender.Draw.PushButton(
            'GUIDE/RIG', self.EVT_GUIDERIG_TAB,
            self.gui_border_locations['left'] + (tab_width*0),
            tab_ypos,
            tab_width, tab_height)
        Blender.Draw.PushButton(
            'COMPS', self.EVT_COMPONENTS_TAB,
            self.gui_border_locations['left'] + (tab_width*1),
            tab_ypos,
            tab_width, tab_height)
        Blender.Draw.PushButton(
            'MENUS', self.EVT_MENU_TAB,
            self.gui_border_locations['left'] + (tab_width*2),
            tab_ypos,
            tab_width, tab_height)
        Blender.Draw.PushButton(
            'XML', self.EVT_XML_TAB,
            self.gui_border_locations['left'] + (tab_width*3),
            tab_ypos,
            tab_width, tab_height)
        Blender.Draw.PushButton(
            'COMPTEST', self.EVT_COMPTEST_TAB,
            self.gui_border_locations['left'] + (tab_width*4),
            tab_ypos,
            tab_width, tab_height)
    
    def _draw_xml_tab_gui(self):
        '''Draw the GUI for the xml tab's contents.
        
        @attention: Make sure only drawing code is within the drawing functions.
        Blender seems to initialize the drawing function (L{self._gui}) many
        times in one session, possibly whenever blender/this gui loses focus.
        '''
        
        # Tab Name
        Blender.Draw.Label(
            'TAB: XML',
            self.gui_border_locations['left'], # X, y, w, h)
            self.gui_border_locations['top'] - 20, # Y - LabelHeight
            self.gui_width, # Width
            20 # Height
        )
    
    ## Defined after the _draw's so it can reference them.
    # Draw Tab Switch, responsible for calling the draw functions for each tab.
    draw_tab_switch = {
        'guiderig':_draw_guiderig_tab_gui,
        'components':_draw_components_tab_gui,
        'menu':_draw_menu_tab_gui,
        'comptest':_draw_comptest_tab_gui,
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
            # Bottom Buttons
            self.EVT_CLOSEGUI_BTN:self.closegui_btn_clicked_event,
            self.EVT_ABOUT_BTN:self.about_btn_clicked_event,
            self.EVT_HELP_BTN:not_handled,
            
            # Tab Buttons
            self.EVT_GUIDERIG_TAB:self.guiderig_tab_clicked_event,
            self.EVT_COMPONENTS_TAB:self.components_tab_clicked_event,
            self.EVT_MENU_TAB:self.menu_tab_clicked_event,
            self.EVT_COMPTEST_TAB:self.rig_tab_clicked_event,
            self.EVT_XML_TAB:self.xml_tab_clicked_event,
            
            # Guide Tab Events
            self.EVT_GUIDERIGTAB_CREATE:
            self.guiderigtab_createguide_clicked_event,
            self.EVT_GUIDERIGTAB_GNAME:not_handled,
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
            'http://code.google.com/p/bcrf/')
        source_url = Blender.Draw.Create(
            'http://github.com/Leefmc/bcrf')
        
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

        Blender.Draw.PupBlock('About BCRF', block)
    
    def closegui_btn_clicked_event(self):
        '''Execute any saving prefs code, then Close the GUI.
        '''
        Blender.Draw.Exit()
    
    def components_tab_clicked_event(self):
        '''Display the Modules Tab.
        '''
        if self.current_tab != 'components':
            self.current_tab = 'components'
            self.redraw_display()
    
    def create_guiderig_clicked_event(self):
        '''The Create Guide button was clicked on the GUIDE/RIG tab.
        '''
        
    
    def display(self):
        '''Display the GUI for the first time.
        '''
        # Currently, there is no difference in the first state and a redraw
        # since all values have defaults. So simply call redraw.
        self.redraw_display()
    
    def guiderig_tab_clicked_event(self):
        '''Display the Guide Tab.
        '''
        if self.current_tab != 'guiderig':
            self.current_tab = 'guiderig'
            self.redraw_display()
    
    def guiderigtab_createguide_clicked_event(self):
        '''The Create/Load Guide button on the Guide/Rig tab was clicked.
        '''
        print 'clicked'
    
    def menu_tab_clicked_event(self):
        '''Display the Rig Tab.
        '''
        if self.current_tab != 'menu':
            self.current_tab = 'menu'
            self.redraw_display()
    
    def redraw_display(self):
        '''Redraw the display GUI.
        '''
        Blender.Draw.Register(self._gui, None, self._events)
    
    def rig_tab_clicked_event(self):
        '''Display the Rig Tab.
        '''
        if self.current_tab != 'comptest':
            self.current_tab = 'comptest'
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

