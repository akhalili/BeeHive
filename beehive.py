__author__ = 'Amirhossein'

import kivy
kivy.require('1.9.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from thermostat import Thermostat


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

    # Each thermostat billboard has a thermostat
    thermostate = Thermostat(APP_KEY)

    def update_billboard(self):
        pass

    def build(self):

        Clock.schedule_interval(self.thermostat.make_request(), 10)


class BeeHiveApp(App):
    def build(self):
        return Button(text='Hello World')

if __name__ == '__main__':
    BeeHiveApp().run()

'''
if __name__ == '__main__':
    main()
'''