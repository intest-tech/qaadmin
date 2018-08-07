from tests.base_testcase import BaseTestCase


class TestIndex(BaseTestCase):
    def test_index(self):
        response = self.client.get('/')
        print(response.data)
