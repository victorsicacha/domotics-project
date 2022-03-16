import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition, SlideTransition, CardTransition, SwapTransition
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.config import Config

Config.set('graphics', 'width', '506')
Config.set('graphics', 'height', '900')


class FloatLayout(FloatLayout):

    def change_screen(self, scr, transition=None, slide=False, direct="left"):
        if slide:
            sm.transition = SlideTransition(direction=direct)
        else:
            sm.transition = transition
        sm.current = scr


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.transition = FadeTransition()


class LoginScreen(Screen):
    def login(self):
        if self.username.text == "domotica" and self.password.text == "macc123":
        #if True:
            sm.current = "home"

        self.username.text = self.password.text = ""


class MainMenu(Screen):
    pass


class Settings(Screen):
    pass


class SideMenu(Screen):
    pass


class Ambients(Screen):
    pass


class Users(Screen):
    pass


class Reminders(Screen):
    pass


class Devices(Screen):
    pass


class Domotica(App):

    def change_screen(self, scr, slide=False, direct="left"):

        if sm.current in ("ambs", "rems", "smenu"):
            if scr == "smenu":
                direct = "right"
            else:
                direct = "left"

        elif sm.current in ("users", "devs", "setts"):
            if scr == "setts":
                direct = "left"
            else:
                direct = "right"

        if slide:
            sm.transition = SlideTransition(direction=direct)

        else:
            sm.transition = FadeTransition()
        sm.current = scr

    def build(self):
        return sm


kv = Builder.load_file("domotica.txt")

sm = WindowManager(transition=FadeTransition())

screens = [LoginScreen(), MainMenu(), Settings(), SideMenu(), Ambients(), Users(), Reminders(), Devices()]
for screen in screens:
    sm.add_widget(screen)

if __name__ == "__main__":
    Domotica().run()
