from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class HomeScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class Manager(ScreenManager):
    pass


kv = Builder.load_file('my.kv')

class MyApp(App):
    def build(self):
        return kv

MyApp().run()
