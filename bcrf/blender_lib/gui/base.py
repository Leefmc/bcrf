''''''

# standard
import copy
# related
import Blender.Draw
# local


class GUI(object):
    ''''''

    def __init__(self, x, y, width, height):
        '''
        '''
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
        #A dict of buttons, used to retrieve values later.
        self._buttons = {}
        
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
    
    def __init__(self, x=0, y=0, width=400, height=500,
                 tab_rows=2, tab_height=15):
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
        '''
        total_tabs = len(self.tabs)
        tab_per_row = int(round(float(total_tabs) / float(self.tab_rows)))
        tab_width = int(round(self.width / tab_per_row))
        tab_row_index = 0
        tab_column_index = 0
        tab_y = self.y
        
        # Draw the Tab Buttons
        for tab_index in range(total_tabs):
            tab_x = self.x + tab_width * tab_column_index
            
            tab = self.tabs[tab_index]
            Blender.Draw.PushButton(
                tab.button_title,
                tab.event_id_base,
                tab_x,
                tab_y,
                tab_width,
                self.tab_height
            )
            
            # Inc the column index
            tab_column_index += 1
            
            # If this is the last column on a row, increase the row index and
            # reset the column.
            if tab_column_index == tab_per_row:
                # If we are on the last row, and there is a modulo, recalculate
                # the positioning data for this new button.
                if (tab_row_index+1 == self.tab_rows-1 
                    and total_tabs % self.tab_rows):
                    tab_per_row = total_tabs - tab_index-1
                    tab_width = self.width / tab_per_row
                
                tab_column_index = 0
                tab_row_index += 1
                tab_y = self.y + tab_row_index * self.tab_height
        
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

class GUIUtilities(object):
    '''A collection of utilities for all that is GUI.'''
    
    def render_menu_string(self, title, menu_items):
        '''Because the menu system uses a rather unfriendly interface, this
        function will take a menu title, menu items, and an optional index list,
        and render out the "Menu String", as seen in the U{menu example
        <blender.org/documentation/246PythonDoc/Draw-module.html#Menu>}.
        
        @param title: The title of the menu.
        @param menu_items: A list of strings representing the menu item titles.
        '''
        # Copy menu items, so we do not modify a reference, if given.
        menu_items = copy.copy(menu_items)
        
        for index in range(len(menu_items)):
            menu_items[index] += ' %x' + str(index)
        menu_items.insert(0, title + ' %t')
        return '|'.join(menu_items)
    
    