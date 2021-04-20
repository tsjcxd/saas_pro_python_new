import pytest
from api.card.brand_member_card import BrandMemberCard
from utils import util
import json


class TestBrandMemberCard:
    @pytest.fixture(autouse=True)
    def setup(self, auto_db):
        self.brand_member_card = BrandMemberCard()
        # yield db

    def test01_create_brand_member_card_success(self, auto_db):
        self.db = auto_db
        payload = self.db.get_fetchone('''SELECT * FROM `create_brand_member_card` WHERE id=1;''')
        payload.update({
            'card_name': '期限卡{}'.format(str(util.get_time())),
            'start_time': util.get_date(0),
            'end_time': util.get_date(7),
        }
        )
        payload.update({'price_gradient': json.loads(payload['price_gradient'])})
        payload.update({'sell_type': json.loads(payload['sell_type'])})
        payload.update({'card_bg': json.loads(payload['card_bg'])})
        payload.update({'admission_shop_list': json.loads(payload['admission_shop_list'])})
        payload.update({'sell_shop_list': json.loads(payload['sell_shop_list'])})
        print(json.dumps(payload, ensure_ascii=False))
        response = self.brand_member_card.create_brand_member_card(json=payload)
        assert response["code"] == 0
        assert response["msg"] == "success"


    # def test02_get_brand_member_card(self):

