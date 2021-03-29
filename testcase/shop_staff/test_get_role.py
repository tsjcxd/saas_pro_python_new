import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from api.shopstaff.get_role import GetRole
from utils.database.db import DB


class TestGetRole:

    def setup(self):
        self.get_role = GetRole()

    def test01_get_role_success(self):
        response = self.get_role.get_role()
        list1 = []
        for i in response.json()['data']['roles']:
            list1.append(i)
        for j in list1:
            if j["name"] == "仅本人":
                role_id = j["id"]
        db = DB()
        db.execute("UPDATE `create_shop_staff` set role_id={} where id=1;".format(role_id))


if __name__ == '__main__':
    TestGetRole()
