__author__ = 'Amirhossein'

import kivy
kivy.require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.properties import ObjectProperty
from thermostat import Thermostat
from kivy.config import Config
from trackbar import TrackBar

Config.set('graphics', 'width', '50')
Config.set('graphics', 'height', '500')


# consts
APP_KEY = unicode('gSeiSW30EV15zvA4efOIjD2lmsSioVz9')


class ThermostatBillboard(Widget):

    temperature = NumericProperty(60)

    # Each thermostat billboard has a thermostat
    thermostat = Thermostat(APP_KEY)

    def __init__(self, **kwargs):
        super(ThermostatBillboard, self).__init__(**kwargs)
        with self.canvas:
            TrackBar(pos=(self.width/2 - 10,10), size=(20, 300))

    def refresh(self, dt):
        temperature = self.thermostat.get_temperature()
        self.temperature = temperature / 10.0

    def terminate(self):
        self.thermostat.terminate()

    def __del__(self):
        self.terminate()


class BeeHiveApp(App):

    billboard = ObjectProperty()

    def build(self):
        self.title = 'BeeHive'
        self.billboard = ThermostatBillboard()
        Clock.schedule_interval(self.billboard.refresh, 10)
        return self.billboard

    def on_stop(self):
        self.billboard.terminate()


if __name__ == '__main__':
    BeeHiveApp().run()