import requests
from until.interceptor.brand_token_interceptor import get_brand_token
from until.interceptor.shop_token_interceptor import get_shop_token


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

    def post(self, api, data=None):
        response = requests.post(api, data=data)
        return response

    def get(self, api, params, **kwargs):
        base_url = "https://saas.test.styd.cn"
        url = base_url + api
        print(url)
        response = requests.get(url, params=params, headers=self.headers, verify=False)
        return response

    def put(self, api, data=None, **kwargs):
        response = requests.put(api, data=data)
        return response
