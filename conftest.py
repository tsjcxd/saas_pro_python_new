import pytest
from conf import test_db_info, auto_db_info
from utils.database.db import DB


@pytest.fixture(scope='class')
def auto_db():
    db = DB(auto_db_info, False)
    print(auto_db_info)
    yield db


@pytest.fixture()
def test_db():
    db = DB(test_db_info, True)
    yield db