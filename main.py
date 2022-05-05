from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.clock import Clock

energy = 100
hours = 4

class Hello(FloatLayout):
    def __init__(self,**kwargs):
        super(Hello,self).__init__(**kwargs)

        self.main_label = Label(text = "Default_text", size_hint=(1, .55),pos_hint={'x':0, 'y':.35})

    #Main Buttons

        self.help_button = Button(text = "Help", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.1},on_press = self.help)
        self.go_button = Button(text = "Go", size_hint=(.3, .1),pos_hint={'x':.05, 'y':.2},on_press = self.go)
        self.say_button = Button(text = "Say", size_hint=(.3, .1),pos_hint={'x':.05, 'y':.1},on_press = self.say)
        self.drive_button = Button(text = "Drive", size_hint=(.3, .1),pos_hint={'x':.65, 'y':.2},on_press = self.drive)

        self.add_widget(self.main_label)

        self.add_widget(self.help_button)
        self.add_widget(self.go_button)
        self.add_widget(self.say_button)
        self.add_widget(self.drive_button)

        self.current_text = ""

    def help(self,event):
        self.main_label.text = "Help"

    def go(self,event):
        self.main_label.text = "Go"

    def say(self,event):
        self.main_label.text = "Say"

    def drive(self,event):
        self.main_label.text = "Drive"

class app1(App):
    def build(self):
        return Hello()
if __name__=="__main__":
     app1().run()