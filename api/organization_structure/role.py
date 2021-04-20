from restclient.restclient import RestClient


class Role:
    def __init__(self):
        self.rest_client = RestClient(is_shop=True)

    def get_role(self):
        response = self.rest_client.get("/_api/v1/common/role/normal")
        return response
