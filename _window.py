from kivy.app import App  # importing app
from kivy.uix.label import Label  # for importing property of text
from kivy.core.window import Window  # to change the display of color

Window.clearcolor = (1,1,1,1)  # To change the color of window from here

class MyAppApp(App):  # naming the name of app that is MyApp
    def build(self):
        label = Label(text='Hello Tyson', font_size='120sp', bold=True, italic = True, color = (1, 0, 0, 2))
        return label

MyAppApp().run()  # to run the class
