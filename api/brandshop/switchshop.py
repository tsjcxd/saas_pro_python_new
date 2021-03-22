from restclient.restclient import RestClient


class SwitchShop:
    def __init__(self):
        self.rest_client = RestClient(is_shop=False)

    def switch_shop(self, data):
        response = self.rest_client.put("/_api/v1/account/switch/shop", data=data)
        return response
