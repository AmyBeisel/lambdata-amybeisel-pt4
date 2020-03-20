
import unittest
from amys_lambda.my_mod import enlarge


class TestMyMod(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(5), 500)
        # self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
    