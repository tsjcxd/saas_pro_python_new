import pytest


class Test:
    @pytest.fixture(autouse=True)
    def setup(self, pre_01):
        self.b_01 = pre_01

    # @pytest.fixture()
    def test01(self):
        c_01 = self.b_01 + 3
        assert c_01 == 4



