from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.navigationdrawer import

KV = '''
Screen:

    NavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Navigation Drawer"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:


        MDNavigationDrawer:
            id: nav_drawer
            
            ContentNavigationDrawer:
                id: cnd
                
                Button: 
                    text: "just testing"
                    on_press: cnd.call_fufu()
                    
                MDList:

                    OneLineListItem:
                        text: "Screen 1"
                        on_press:
                            root.nav_drawer.set_state("close")
                            root.screen_manager.current = "scr 1"
        
                    OneLineListItem:
                        text: "Screen 2"
                        on_press:
                            root.nav_drawer.set_state("close")
                            root.screen_manager.current = "scr 2"
            
'''


class ContentNavigationDrawer(BoxLayout):
    def call_fufu(self):
        print("pressed")



class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)



TestNavigationDrawer().run()
