from . import BaseTestCase

from doppelbot import doppelbot


class TestDoppelbot(BaseTestCase):

    def test_something(self):
        self.assertEquals(
            'Hello World!',
            doppelbot(),
        )
