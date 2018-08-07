from tests.base_testcase import BaseTestCase


class TestIndex(BaseTestCase):
    def test_index(self):
        response = self.client.get('/')
        # todo: assertion
        print(response.data)
