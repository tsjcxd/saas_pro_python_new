import os
import requests
import configparser

from public.get_token import get_shop_token
from public.get_token import get_brand_token


class RestClient:
    def __init__(self, is_shop=True):
        if is_shop:
            token = get_shop_token()
        else:
            token = get_brand_token()
        self.headers = {
            "app-id": "11111",
            "app-version": "11111",
            "token": token
        }
        print(self.headers)

    def test_reader_environment_ini(self):
        self.base_dir = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
        print(self.base_dir)
        self.config = configparser.ConfigParser()
        self.text = os.path.join(self.base_dir, 'conf')
        self.config.read(os.path.join(self.text, "env.ini"))
        self.base_url = self.config.get(section='environment', option='test_baseurl')
        return self.base_url

    def post(self, api, data=None, **kwargs):
        base_url = RestClient.test_reader_environment_ini(self)
        url = base_url + api
        response = requests.post(api, data=data, verify=False)
        return response

    def get(self, api, params, **kwargs):
        base_url = RestClient.test_reader_environment_ini(self)
        url = base_url + api
        response = requests.get(url, params=params, headers=self.headers, verify=False)
        return response

    def put(self, api, data=None, **kwargs):
        base_url = RestClient.test_reader_environment_ini(self)
        url = base_url + api
        response = requests.put(url, data=data, verify=False)
        return response
