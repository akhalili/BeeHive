__author__ = 'Amirhossein'

from thermostat import Thermostat

# consts
APP_KEY = unicode('gSeiSW30EV15zvA4efOIjD2lmsSioVz9')

def main():

    # init thermostat
    thermostat = Thermostat(APP_KEY)
    thermostat.make_request()

    print ('wait to finish')
    raw_input('press a key')

    del thermostat


    print('main Finished')


if __name__ == '__main__':
    main()
