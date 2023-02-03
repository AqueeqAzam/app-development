from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MyTextInputApp(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical', padding=200, spacing=20)

        self.email = TextInput(text = 'Enter your Email')
        self.passw = TextInput(text='Enter your password')
        self.submit = Button(text= 'Log In',  on_press = self.submitbtn)


        layout.add_widget(self.email)
        layout.add_widget(self.passw)
        layout.add_widget(self.submit)


        return layout

    def submitbtn(self,obj):
        print('Your Email is =', self.email.text)
        print('Your password is =', self.passw.text)




MyTextInputApp().run()
