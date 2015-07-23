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
        pin_code = data['ecobeePin']
        expired_mins = data['expires_in']
        self.authorization_token = data['code']

        print('In ' + str(expired_mins) +' Please register the app with pin code ' + pin_code + ' in your ecobee portal at http:////www.ecobee.com')
        raw_input('Press enter to continue...')


        # Request access and refresh tokens
        token_params = {'grant_type': u'ecobeePin', 'code': self.authorization_token, 'client_id': self.api_key}
        data = self.post('token', params=token_params)
        self.accesss_token = data['access_token']
        self.token_type = data['token_type']
        self.refresh_token = data['refresh_token']
        self.expires_in = data['expires_in']

        with open('./config.txt','w') as config_file:
            json.dump(data, config_file, ensure_ascii=False)


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

        url = ECOBEE_URL + task + '?grant_type=ecobeePin&code=' + self.authorization_token + '&client_id=' + self.api_key
        response = requests.post(url)
        parsed_response = response.json()

        return parsed_response





