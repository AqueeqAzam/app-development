from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyButtonApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)
        btn1 = Button(text='Button 1')
        btn2 = Button(text='Button 2')
        btn3 = Button(text='Button 3')
        btn4 = Button(text='Button 4')

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        return layout

MyButtonApp().run()
