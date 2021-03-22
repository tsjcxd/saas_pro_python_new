import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from api.brandshop.getbrandshop import GetBrandShop
from utils.database.db import get_data
import pytest


class TestGetBrandShop:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.get_brand_shop = GetBrandShop()

    def test_get_brand_shop(self):
        result = get_data("SELECT * FROM `GetBrandShop`;")
        params = result
        response = self.get_brand_shop.get_brand_shop(params=params)
        print(response.json())

# if __name__ == "__main__":
#     TestGetBrandShop()
