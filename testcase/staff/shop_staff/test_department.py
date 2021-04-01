import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from api.staff.shopstaff.get_department import GetDepartment


@pytest.fixture(scope='module')
def create_department():
    


class TestInit:




class TestDepartmentCreate:
    pass


class TestDepartmentEdit:
    pass


class TestGetDepartment:

    def setup(self):
        self.get_department = GetDepartment()

    def test01_get_department_sales_success(self):
        response = self.get_department.get_department()
        department = response.json()['data']['department']
        dict1 = {}
        for i in department:
            dict1[i["name"]] = i["id"]
        id = dict1["销售部"]
        print(id)

class TestDepartmentDelete:
    pass


if __name__ == '__main__':
    TestGetDepartment()
