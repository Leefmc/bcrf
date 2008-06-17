''''''

# standard
# related
import Blender.Draw
# local


class GUI(object):
    ''''''

    def __init__(self, x=0, y=0, width=200, height=400):
        '''
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        self._keyboard_event_switch = {
            Blender.Draw.ESCKEY:self._esc_key_event
        }
        self._gui_event_switch = {}
    
    def _gui_events(self, event_id):
        '''Call the gui event switch.
        '''
        if self._gui_event_switch.has_key(event_id):
            self._gui_event_switch[event_id](event_id)
    
    def _esc_key_event(self, event_id, event_value):
        '''
        '''
        Blender.Draw.Exit()
    
    def _keyboard_events(self, event_id, event_value):
        '''Call the keyboard event switch.
        '''
        if self._keyboard_event_switch.has_key(event_id):
            self._keyboard_event_switch[event_id](event_id, event_value)
    
    def draw(self):
        '''Draw the GUI.
        @note: This base is ment to be overloaded since this base doesn't
        actually draw anything.
        '''
        pass
    
    def register(self):
        '''Register this GUI.
        '''
        Blender.Draw.Register(
            self.draw, self._keyboard_events, self._gui_events
        )
    
    def redraw(self):
        '''Redraw the GUI.
        '''

class TabContainer(GUI):
    ''''''
    
    def __init__(self, x=0, y=0, width=300, height=400,
                 tab_rows=1, tab_height=15):
        '''
        '''
        super(TabContainer, self).__init__(x, y, width, height)
        
        self.tab_rows = tab_rows
        self.tab_height = tab_height
        
        self.content_pad = tab_height * tab_rows
        
        self.tabs = []
        self.active_tab = None
        
        self.tabs_event_id_base_index = 1100
    
    def add_tab(self, tab_content):
        '''Add a L{TabContent tab} in this container.
        
        @param tab_content: The L{TabContent} being added.
        '''
        self.tabs.append(tab_content)
        
        # Add the tab's events, to this container's.
        for tab_event_id in tab_content._gui_event_switch:
            self._gui_event_switch[tab_event_id] = tab_content.\
                _gui_event_switch[tab_event_id]
        
        if self.active_tab is None:
            self.active_tab = tab_content
        
    
    def draw(self):
        '''
        @important: At the moment, rows do not work. So even if given multiple
        rows, this draw will only put buttons in one row.
        '''
        total_tabs = len(self.tabs)
        tab_button_width = int(round(self.width / total_tabs))
        
        # Draw the Tab Buttons
        for tab_index in range(total_tabs):
            tab = self.tabs[tab_index]
            Blender.Draw.PushButton(
                tab.button_title,
                tab.event_id_base,
                self.x + tab_button_width * tab_index, # +1 offsets zero.
                self.y,
                tab_button_width,
                self.tab_height
            )
        
        # Draw the Active Tab
        self.active_tab.draw()
    
    def request_event_id_base(self):
        '''This is used by TabContents to give them a base id. Ie, TabA's
        contents will all use 1100-1199 because it was given the "1100" series
        by this function.
        '''
        eid_base = self.tabs_event_id_base_index
        self.tabs_event_id_base_index += 100
        return eid_base

class TabContent(GUI):
    '''
    '''
    
    
    tab_header = None
    button_title = None
    
    def __init__(self, tab_container):
        '''
        '''
        super(TabContent, self).__init__(
            tab_container.x,
            tab_container.y + tab_container.content_pad,
            tab_container.width,
            tab_container.height - tab_container.content_pad
        )
        
        self.tab_container = tab_container
        self.event_id_base = tab_container.request_event_id_base()
        
        tab_container._gui_event_switch[
            self.event_id_base] = self.tab_active_event
    
    def _true_eid(self, generic_id):
        '''
        '''
        return self.event_id_base + generic_id

    def draw(self):
        '''
        '''
        Blender.Draw.Label('Tab: %s' % self.tab_header,
                               self.x, self.y + self.height, 200, 25)
    
    def tab_active_event(self, event_id):
        '''
        '''
        self.tab_container.active_tab = self
        Blender.Draw.Redraw()

