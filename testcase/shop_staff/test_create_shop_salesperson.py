from api.shopstaff.create_salesperson import CreateSalesperson
from utils.util import random_name, random_phone
from utils.database.db import query, update


class TestCreateShopSalesperson:

    def setup(self):
        self.salesperson = CreateSalesperson()

    def test01_create_shop_salesperson_success(self):
        update("UPDATE `create_shop_staff` set staff_name={} where id=1".format(str(random_name())))
        update("UPDATE `create_shop_staff` set mobile={} where id=1".format(str(random_phone())))
        update("UPDATE `create_shop_staff` set nickname={} where id=1".format(str(random_name())))


if __name__ == '__main__':
    TestCreateShopSalesperson()