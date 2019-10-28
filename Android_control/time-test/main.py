import kivy.app
import kivy.uix.boxlayout
import kivy.uix.textinput
import kivy.uix.label
import kivy.uix.button

import requests
import time

class SimpleApp(kivy.app.App):
    def build(self):
        self.label = kivy.uix.label.Label(text="Measured Time:")
        self.button = kivy.uix.button.Button(text="Measure time of reaction")
        self.button.bind(on_press=self.http_ping)
        self.boxLayout = kivy.uix.boxlayout.BoxLayout(orientation="vertical")
        self.boxLayout.add_widget(self.label)
        self.boxLayout.add_widget(self.button)
        return self.boxLayout
    def http_ping(self, btn):
        self.label.text = self.textInput.text
if __name__ == "__main__":
    simpleApp = SimpleApp()
    simpleApp.run()