from restclient.restclient import RestClient


class Department:
    def __init__(self):
        self.rest_client = RestClient(is_shop=True)

    def get_department(self):
        response = self.rest_client.get("/_api/v1/department")
        return response
