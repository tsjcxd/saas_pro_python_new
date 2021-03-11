import requests
import configparser
import os
import warnings

warnings.filterwarnings("ignore")


# 读取配置文件environment.ini的baseUrl
def reader_environment_ini():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config = configparser.ConfigParser()
    text = os.path.join(base_dir, 'conf')
    config.read(os.path.join(text, "environment.ini"))
    result = config.get(section='environment', option='test_baseurl')
    return result


# 读取配置文件request_base.ini的baseUrl
def reader_request_base_ini():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config = configparser.ConfigParser()
    text = os.path.join(base_dir, 'conf')
    config.read(os.path.join(text, "request_base.ini"))
    result = config.get(section='url_header', option='brand_token')
    # print(result)
    return result


# 更新配置文件request_base.ini的shop_token和获取brand_token
def set_request_base_ini(result):
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    config = configparser.ConfigParser()
    text = os.path.join(base_dir, 'conf')
    config.read(os.path.join(text, "request_base.ini"))
    config.set("url_header", "shop_token", result)
    config.write(open(os.path.join(text, "request_base.ini"), "r+"))


def get_shop_token():
    url = reader_environment_ini() + "/_api/v1/account/switch/shop"
    print(url)

    header = {
        "app-id": "11111",
        "app-version": "11111",
        "token": "{}".format(reader_request_base_ini())
    }
    data = {"shop_id": "272505760186663"}
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    response = requests.put(url=url, json=data, headers=header, verify=False)
    token = (response.json()['data']['token'])
    return token
    set_request_base_ini(token)


if __name__ == '__main__':
    get_shop_token()
