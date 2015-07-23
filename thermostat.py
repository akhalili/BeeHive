__author__ = 'Amirhossein'

import json
import requests

# Consts
ECOBEE_URL = 'https://api.ecobee.com/'

class Thermostat:

    def __init__(self, api_key):

        self.api_key = api_key
        self.authorize()

    # authorize the thermostart
    def authorize(self):

        # Request authorization
        authorization_params = {'response_type': 'ecobeePin', 'client_id': self.api_key, 'scope': 'smartWrite'}
        data = self.get('authorize', params=authorization_params)
        self.pin_code = data['ecobeePin']
        expired_mins = data['expires_in']

        print('In ' + str(expired_mins) +' Please register the app with pin code ' + self.pin_code + ' in your ecobee portal at http:////www.ecobee.com')
        raw_input('Press enter to continue...')


        # Request access and refresh tokens
        token_params = {'grant_type': 'refresh_token', 'code': self.pin_code, 'client_id': self.api_key}
        data = self.post('token', params=token_params)
        self.accesss_token = data['access_token']
        self.token_type = data['token_type']
        self.refresh_token = data['refresh_token']
        self.expires_in = data['expires_in']


    # Communicate with ecobee using the url
    # url: the url to communicate with ecobee
    # returns: json parsed response
    def get(self, task, params):

        url = ECOBEE_URL + task
        response = requests.get(url, params)
        parsed_response = response.json()

        return parsed_response


    # Communicate with ecobee using the url
    # url: the url to communicate with ecobee
    # returns: json parsed response
    def post(self, task, params):

        url = ECOBEE_URL + task
        response = requests.post(url, data=json.dumps(params))
        parsed_response = response.json()

        return parsed_response





