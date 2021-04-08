from restclient.restclient import RestClient


class CreateBrandMemberCard:
    def __init__(self):
        self.rest_client = RestClient(is_shop=False)

    def create_brand_member_card(self, data=None, **kwargs):
        response = self.rest_client.post("/v1/cards/member/brand", data=data, **kwargs)
        return response
