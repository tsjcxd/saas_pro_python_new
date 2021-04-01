import pytest
import datetime
import json

from api.shopstaff.create_salesperson import CreateSalesperson
from utils.util import random_name, random_phone
from utils.database.db import DB


@pytest.fixture(scope='class')
def create_db():
    db = DB()
    yield db
    db.close()


@pytest.mark.usefixtures('create_db')
class TestCreateShopSalesperson:

    @pytest.fixture(autouse=True)
    def setup(self, create_db):
        self.db = create_db
        self.salesperson = CreateSalesperson()

    def test01_create_shop_salesperson_success(self):
        payload = self.db.get_fetchone('''SELECT * FROM create_shop_staff WHERE id=1;''')
        print(payload)
        name = random_name()
        # print((json.dumps(payload)))
        payload.update(role_id=json.loads((payload['role_id'])))
        payload.update(image_avatar=json.loads((payload['image_avatar'])))
        payload.update(image_face=json.loads((payload['image_face'])))
        print(payload)
        # print(payload)
        payload.update({
            'staff_name': name,
            'mobile': random_phone(),
            'nickname': name,
            # 'entry_date': datetime.datetime.now()
        })
        payload.pop('identity')
        payload.pop('entry_date')
        print(json.dumps(payload, ensure_ascii=False))
        #
        # data = self.db.get_fetchone('SELECT * FROM `create_shop_staff` where id = 1;')
        response = self.salesperson.create_salesperson(json=payload)
        print(response.text)



if __name__ == '__main__':
    TestCreateShopSalesperson()

