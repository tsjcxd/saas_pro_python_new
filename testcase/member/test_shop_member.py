import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from utils.util import random_name, random_phone
from api.member.shop_member import ShopMember
import pytest


class TestShopMemberCase:
    """新增门店会员（门店：汤汤上海店）"""

    @pytest.fixture()
    def setup(self):
        self.shopMember = ShopMember()

    def test01_create_shopMember_success(self, setup):
        payload = {
            "member_name": random_name(5, "会员"),
            "mobile": random_phone()
        }
        response = self.shopMember.create_shop_member(json=payload)
        print(response.json())
        assert response.json()["msg"] == "success"
        assert response.json()["code"] == 0
        return response.json()["data"]["info"]["member_id"]

# if __name__ == '__main__':
#     TestCreateShopMemberCase()
