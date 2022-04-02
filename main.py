from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import kivy

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text = "Name: "))
        self.name = TextInput(multiline = False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text = "Email: "))
        self.email = TextInput(multiline = False)
        self.inside.add_widget(self.email)

        self.inside.add_widget(Label(text = "Password: "))
        self.password = TextInput(multiline = False)
        self.inside.add_widget(self.password)
        
        self.add_widget(self.inside)


        self.submit= Button(text = "Submit", font_size=40)
        self.submit.bind(on_press = self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        print(name)
        self.name.text = ""

        
class SocialApp(App):
    def build(self):
        return Grid()

if __name__ == "__main__":
    SocialApp().run()
