__author__ = 'Amirhossein'

from thermostat import Thermostat

# consts
APP_KEY = unicode('gSeiSW30EV15zvA4efOIjD2lmsSioVz9')

def main():

    # init thermostat
    thermostat = Thermostat(APP_KEY)
    thermostat.make_request()

    raw_input('wait:')


if __name__ == '__main__':
    main()
