from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Grid(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print(self.name.text)
        print(self.email.text)
        self.name.text = ""
        self.email.text = ""
        


class SocialApp(App):
    def build(self):
        return Grid()
    
if __name__ == "__main__":
    SocialApp().run()