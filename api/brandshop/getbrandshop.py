from restclient.restclient import RestClient


class GetBrandShop:
    def __init__(self):
        self.rest_client = RestClient(is_shop=False)

    def get_brand_shop(self, params, **kwarg):
        response = self.rest_client.get("/_api/v1/shop", params=params, **kwarg)
        return response
