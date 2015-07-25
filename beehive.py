__author__ = 'Amirhossein'

import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
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



class MyApp(App):
    def build(self):
        return Button(text='Hello World')

if __name__ == '__main__':
    MyApp().run()

'''
if __name__ == '__main__':
    main()
'''