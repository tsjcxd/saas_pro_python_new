from restclient.restclient import RestClient


class Shop:
    def __init__(self):
        self.rest_client = RestClient(is_shop=True)

    def get_shop(self):
        response = self.rest_client.get("/_api/v1/staff/brand/select_shop_list")
        return response
