import pytest


@pytest.fixture(scope='function')
def pre_01():
    a_01 = 1
    print(a_01)
    yield a_01


@pytest.fixture()
def pre_02():
    a_02 = 2
    print(a_02)
    yield a_02