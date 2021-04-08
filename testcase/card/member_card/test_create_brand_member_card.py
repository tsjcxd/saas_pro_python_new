import pytest
from api.card.member_card.create_brand_member_card import CreateBrandMemberCard
from utils.database.db import DB
from utils import  util



@pytest.fixture(scope='class')
def create_db():
    db = DB()
    yield db
    db.close()


@pytest.mark.usefixtures('create_db')
class TestCreateBrandMemberCard:

    @pytest.fixture(autouse=True)
    def setup(self, create_db):
        self.db = create_db
        self.brand_member_card = CreateBrandMemberCard()

    def test01_create_brand_member_card_success(self):
        payload = self.db.get_fetchone('''SELECT * FROM `create_brand_member_card` WHERE id=1;''')
        payload.update({
            'card_name': util.random_name('期限卡'),
            'start_time': util.get_date(0),
            'end_time': util.get_date(7),
        }
        )
        print(payload)
