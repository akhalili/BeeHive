__author__ = 'Amirhossein'

import json
import requests
import datetime

# Consts
ECOBEE_URL = 'https://api.ecobee.com/'

class Thermostat:

    def __init__(self, api_key):

        self.api_key = api_key

        self.read_author_config_file()

        if datetime.datetime.now() > self.expires:
            self.authorize()

    # authorize the thermostat
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
        token_params = {'grant_type':'ecobeePin', 'code': self.authorization_token, 'client_id': self.api_key}
        data = self.post('token', params=token_params)
        self.accesss_token = data['access_token']
        self.token_type = data['token_type']
        self.refresh_token = data['refresh_token']
        self.expires = datetime.datetime.now() + datetime.timedelta(minutes=data['expires_in'])

        # update the authorization config file
        self.update_author_config_file()

    # Update the authorization config file
    def update_author_config_file(self):
        with open('./AutoConfig.txt','wb') as config_file:
            data = {'access_token': self.accesss_token, 'token_type': self.token_type, 'refresh_token': self.refresh_token, 'expires': self.expires.strftime('%Y-%m-%d %H:%M:%S')}
            json.dump(data, config_file, ensure_ascii=False)

    # Read the authorization config file
    def read_author_config_file(self):

        data = []
        with open('./AutoConfig.txt','rb') as config_file:
            data = json.load(config_file)

        self.accesss_token = data['access_token']
        self.token_type = data['token_type']
        self.refresh_token = data['refresh_token']
        self.expires = datetime.datetime.strptime(data['expires'],'%Y-%m-%d %H:%M:%S')

        return data

    # get a task and parameters to ecobee
    # task: the task
    # params: parameters to send
    # returns: json parsed response
    def get(self, task, params):

        url = ECOBEE_URL + task
        response = requests.get(url, params)
        parsed_response = response.json()

        return parsed_response

    # post a task and parameters to ecobee
    # task: the task
    # params: parameters to send
    # returns: json parsed response
    def post(self, task, params):

        url = ECOBEE_URL + task
        response = requests.post(url, params=params)
        parsed_response = response.json()

        return parsed_response





