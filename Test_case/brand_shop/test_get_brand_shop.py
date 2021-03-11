import sys
import os
from Api.brand_shop.get_brand_shop import GetBrandShop
from until.database.jdbc_ssh_channel import get_data
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


class TestGetBrandShop(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.get_brand_shop = GetBrandShop()

    def test_get_brand_shop(self):
        result = get_data("SELECT * FROM `GetBrandShop`;")
        params = result
        response = self.get_brand_shop.get_brand_shop(params=params)
        print(response.json())


if __name__ == "__main__":
    TestGetBrandShop()
