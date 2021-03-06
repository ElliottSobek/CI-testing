import unittest
from decimal import Decimal

from teamcity import is_running_under_teamcity
from teamcity.unittestpy import TeamcityTestRunner

from main import Main


class TestMain(unittest.TestCase):
    main = Main()

    def test_add_good(self):
        self.assertEqual(2, self.main.add(1, 1))

    def test_add_bad(self):
        self.assertNotEqual(1, self.main.add(1, 1))

    def test_double_good(self):
        self.assertEqual(4, self.main.double(2))

    def test_double_bad(self):
        self.assertNotEqual(1, self.main.double(2))

    def test_root_bad(self):
        self.assertEqual(Decimal("2"), self.main.root(4))

    def test_root_good(self):
        self.assertNotEqual(Decimal("1"), self.main.root(2))


if __name__ == '__main__':
    if is_running_under_teamcity():
        runner = TeamcityTestRunner()
    else:
        runner = unittest.TextTestRunner()
    unittest.main(testRunner=runner)
