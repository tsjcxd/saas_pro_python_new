from restclient.restclient import RestClient


class ShopMember:
    def __init__(self):
        self.rest_client = RestClient(is_shop=True)

    def create_shop_member(self, data=None, **kwargs):
        response = self.rest_client.post("/_api/v1/member", data=data, **kwargs)
        return response
