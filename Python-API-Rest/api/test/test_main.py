from flask_testing import TestCase
from flask import current_app as app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        return app

    def test_1(self):
        return self.assertTrue(True)

    def setUp(self):
        pass

    def tearDown(self):
        pass