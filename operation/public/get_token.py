import urllib3
import requests
from conf import base_url, app_id, app_version, name, password, nvc_val


def get_brand_token():
    """获取品牌维度的token"""
    url = base_url + "/_api/login/account"
    header = {
        "app-id": app_id,
        "app-version": app_version
    }
    data = {
        "name": name,
        "password": password,
        "nvc_val": nvc_val
    }
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.post(url=url, headers=header, data=data, verify=False)
    token = (response.json()['data']['token'])
    return token


def get_shop_token():
    """获取门店维度的token"""
    url = base_url + "/_api/v1/account/switch/shop"

    header = {
        "app-id": app_id,
        "app-version": app_version,
        "token": "{}".format(get_brand_token())
    }
    data = {
        "shop_id": "272505760186663"
    }
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.put(url=url, json=data, headers=header, verify=False)
    token = (response.json()['data']['token'])
    return token


# if __name__ == '__main__':
#     get_shop_token()
