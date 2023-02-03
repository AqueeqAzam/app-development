from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):
        btn = Button(text='Click me', size_hint= (0.3,0.4),
                     font_size = '44sp', on_press=self.btn_click)  # or you may define on_release= self.btn_click
        return btn

    def btn_click(self, btn):
        print('Button click')
ButtonApp().run()
