from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.navigationdrawer import NavigationLayout,MDNavigationDrawer
from kivymd.uix.button import Button, MDRaisedButton
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget

KV = '''
<ContentNavigationDrawer>:
    ScrollView:

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
       
             
Screen:
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        elevation: 10
        title: "MDNavigationDrawer"
        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

    NavigationLayout:
        ScreenManager:
            id: screen_manager
            
            Screen:
                id: register_screen
                name: "scr 1"
                
                MDRaisedButton:
                    id: connect_button
                    text:"Photo"
                    #size_hint: 0.1, 0.3
                    pos_hint: {"x":0.5, "top":0.5}
                    background_normal: ''
                    background_down: ''
                    on_press: app.Connect()
                

            Screen:
                name: "scr 2"

                MDLabel:
                    text: "Screen 2"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
                
                
                
               
             
'''

class ContentNavigationDrawer(BoxLayout):
        pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Green"  # "Purple", "Red"
        return Builder.load_string(KV)

    def Connect(self):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.0.10', 1234))

        msg = s.recv(1024)
        print(msg.decode("utf-8"))





MyApp().run()
