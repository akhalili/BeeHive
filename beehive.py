__author__ = 'Amirhossein'

import kivy
kivy.require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import NumericProperty
from thermostat import Thermostat
from kivy.config import Config

Config.set('graphics', 'width', '100')
Config.set('graphics', 'height', '500')


# consts
APP_KEY = unicode('gSeiSW30EV15zvA4efOIjD2lmsSioVz9')

def main():

    # init thermostat
    thermostat = Thermostat(APP_KEY)
    thermostat.make_request()

    print ('wait to finish')
    raw_input('press a key')

    thermostat.__del__()


    print('main Finished')

class ThermostatBillboard(Widget):

    temperature = NumericProperty(60)

    # Each thermostat billboard has a thermostat
    thermostat = Thermostat(APP_KEY)

    def refresh(self, dt):
        temperature = self.thermostat.get_temperature()
        self.temperature = temperature / 10.0

    def __del__(self):
        thermostat.__del__()


class BeeHiveApp(App):
    def build(self):
        billboard = ThermostatBillboard()
        Clock.schedule_interval(billboard.refresh, 10)
        return billboard

if __name__ == '__main__':
    BeeHiveApp().run()

'''
if __name__ == '__main__':
    main()
'''