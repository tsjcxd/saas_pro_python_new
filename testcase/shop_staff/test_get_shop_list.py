import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from api.shopstaff.get_shop_list import GetShop
from utils.database.db import DB


class TestGetShopList:

    def setup(self):
        self.get_shop = GetShop()

    def test01_get_shop_success(self):
        response = self.get_shop.get_shop()
        list1 = []
        for i in response.json()['data']['list']:
            list1.append(i)
        for j in list1:
            if j["shop_name"] == "汤汤上海店":
                shop_id = j["shop_id"]
        db = DB()
        db.execute("UPDATE `create_shop_staff` set shop_id={} where id=1;".format(shop_id))


if __name__ == '__main__':
    TestGetShopList()