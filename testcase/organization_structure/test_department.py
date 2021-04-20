import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from api.organization_structure.department import Department


@pytest.fixture(scope='module')
class TestDepartment:
    """获取部门"""
    def setup(self):
        self.get_department = Department()

    def test01_get_department_sales_success(self):
        response = self.get_department.get_department()
        department = response.json()['data']['department']
        dict1 = {}
        for i in department:
            dict1[i["name"]] = i["id"]
        id = dict1["销售部"]
        print(id)



if __name__ == '__main__':
    TestDepartment()
