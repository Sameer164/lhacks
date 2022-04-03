from ast import Pass
import code
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





class Questionnaire(Screen):
    def on_spinner_select(self,text, a):
        p = Password_saver()
        if a == "g":
            p.gender(text)
        elif a == "p":
            p.preference(text)
        else:
            p.age(text)
        return 


class Login(Screen):
    code = ObjectProperty(None)
    p = Password_saver()
    def valid(self):
        if self.p.is_valid(self.code):
            self.p.login(self.code)
            return True
        else:
            return False

    



class WindowManager(ScreenManager):
    pass



class Profile(Screen):
    pass



class MyMainApp(App):
    def build(self):
        return Builder.load_file("my.kv")


if __name__ == "__main__":
    MyMainApp().run()