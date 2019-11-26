import kivy.app
import kivy.uix.boxlayout
import kivy.uix.textinput
import kivy.uix.label
import kivy.uix.button
from kivy.logger import Logger

from kivy.logger import Logger

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
        print("onpress")
        Logger.debug('sending the request')
        begin=time.time()
        requests.get("http://192.168.4.1")
        self.label.text = str(time.time()-begin)
if __name__ == "__main__":
    simpleApp = SimpleApp()
    simpleApp.run()