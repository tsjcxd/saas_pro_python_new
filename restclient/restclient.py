
import requests

from public.get_token import get_shop_token
from public.get_token import get_brand_token
from conf import base_url


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
        # print(self.headers)

    def post(self, api, data=None, **kwargs):
        url = base_url + api
        response = requests.post(url, data=data, headers=self.headers, verify=False)
        return response

    def get(self, api, params=None, **kwargs):
        url = base_url + api
        response = requests.get(url, params=params, headers=self.headers, verify=False)
        return response

    def put(self, api, data=None, **kwargs):
        url = base_url + api
        response = requests.put(url, data=data, headers=self.headers, verify=False)
        return response
