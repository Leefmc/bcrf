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
    
    def draw(self):
        '''
        '''
        

class TabContainer(GUI):
    ''''''
    
    def __init__(self, x=0, y=0, width=200, height=400,
                 tab_rows=2, tab_height=15):
        '''
        '''
        super(TabContainer, self).__init__(x, y, width, height)
        
        self.tab_rows = tab_rows
        self.tab_height = tab_height
    
    def _register_tab(self, tab_content):
        '''Register a L{TabContent tab} in this container.
        
        @param tab_content: The L{TabContent} being registered.
        
        @important: Users do not need to call this function. Upon Initialization
        of a L{TabContent} class, this function is called on the container
        given to the L{TabContent} class, by the TabContent class.
        '''
        

class TabContent(GUI):
    ''''''
    
    def __init__(self, tab_container, tab_header, button_title):
        '''
        '''
        super(TabContainer, self).__init__(x, y, width, height)
        self.tab_header = tab_header
        self.button_title = button_title

