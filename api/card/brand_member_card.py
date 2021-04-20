from restclient.restclient import RestClient


class BrandMemberCard:
    def __init__(self):
        self.rest_client = RestClient(is_shop=False)

    def create_brand_member_card(self, data=None, **kwargs):
        response = self.rest_client.post("/_api/v1/cards/member/brand", data=data, **kwargs)
        return response

    def get_brand_member_card(self, card_id, **kwargs):
        response = self.rest_client.get("/_api/v1/cards/member/brand/{}".format(card_id), **kwargs)
        return response