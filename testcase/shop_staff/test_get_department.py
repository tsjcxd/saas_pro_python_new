import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from api.shopstaff.get_department import GetDepartment
from utils.database.db import DB


class TestGetDepartment:

    def setup(self):
        self.get_department = GetDepartment()

    def test01_get_department_sales_success(self):
        response = self.get_department.get_department()
        list1 = []
        for i in response.json()['data']['department']:
            list1.append(i)
        for j in list1:
            if j["name"] == "销售部":
                department_id = j["id"]
        db = DB()
        db.execute("UPDATE `create_shop_staff` set department_id={} where id=1;".format(department_id))


if __name__ == '__main__':
    TestGetDepartment()
