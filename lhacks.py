from ast import Pass
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from validate import Password_saver
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.base import runTouchApp
from kivy.uix.spinner import Spinner


class MainWindow(Screen):
    named = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    latest = ""

    def good(self):
        p = SecondWindow()
        if (self.named.text != "" and self.named!= None) and (self.email.text != "" and self.email != None) and (self.password.text != "" and self.password != None):
            p = Password_saver()
            MainWindow.latest = str(p.first_time_users(self.named.text, self.email.text, self.password.text))
            self.named.text = ""
            self.email.text = ""
            self.password.text = ""
            return True
        else:
            self.named.text = ""
            self.email.text = ""
            self.password.text = ""
            return False


class SecondWindow(Screen):
    
    def get_code(self):
        p = Password_saver()
        return p.get_code_last()




class drop_content(DropDown):
    pass

class Questionnaire(Screen):
    # spinner = Spinner(
    #     # default value shown
    #     text='Home',
    #     # available values
    #     values=('Home', 'Work', 'Other', 'Custom'),
    #     # just for positioning in our example
    #     size_hint=(None, None),
    #     size=(100, 44),
    #     pos_hint={'center_x': .5, 'center_y': .5}
    # )

    # runTouchApp(spinner)
    pass



    



class WindowManager(ScreenManager):
    pass




kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()