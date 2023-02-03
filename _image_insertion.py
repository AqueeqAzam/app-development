from kivy.app import App
from kivy.uix.image import Image

class MyImageApp(App):
    def build(self):
        img = Image(source='computers-linux-wallpaper-preview.jpg', size_hint = (None, None),
                    width=1100,height=900)
        return img

MyImageApp().run()
