from restclient.restclient import RestClient


class CreateSalesperson:

    def __init__(self, is_shop=True):
        self.rest_client = RestClient()

    def create_salesperson(self, data=None, **kwargs):
        response = self.rest_client.post("/_api/v1/staff/shop/basic", data=data, **kwargs)
        return response
