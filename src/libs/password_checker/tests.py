import unittest
from .checker import check_length


class TestPasswordChecker(unittest.TestCase):
    """
        [BASE]
    """

    @classmethod
    def setUpClass(cls):
        cls.password_nok = "ABC1@"
        cls.password_ok = "AbCdEfGh@2"

    def test_check_length(self):
        result = check_length(self.password_ok)
        self.assertEqual(result["type"], "length")
        self.assertEqual(result["error"], None)

        result = check_length(self.password_nok)
        self.assertEqual(result["type"], "length")
        self.assertNotEqual(result["error"], None)
        self.assertEqual(type(result["error"]), str)


if __name__ == '__main__':
    unittest.main()
