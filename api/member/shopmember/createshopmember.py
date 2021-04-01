from restclient.restclient import RestClient


class CreateShopMember:
    def __init__(self):
        self.rest_client = RestClient(is_shop=True)

    def create_shop_member(self, data, **karges):
        response = self.rest_client.post("/_api/v1/member", data=data)
        return response
