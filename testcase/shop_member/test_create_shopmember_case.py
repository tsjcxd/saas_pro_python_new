import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.util import random_name, random_phone
from api.shopmember.createshopmember import CreateShopMember
import pytest


class TestCreateShopMemberCase:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.shopmember = CreateShopMember()

    def test01_create_shopmember_success(self):
        payload = {
            "member_name": random_name(),
            "mobile": random_phone()
        }
        response = self.shopmember.create_shop_member(data=payload)
        assert response.json()["msg"] == "success"
        assert response.json()["code"] == 0
        return response.json()["data"]["info"]["member_id"]


# if __name__ == '__main__':
#     TestCreateShopMemberCase()
