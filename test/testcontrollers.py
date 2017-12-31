from controllers import monty
import unittest

class TestController(unittest.TestCase):
    def test_choose(self):
        random_num = monty.choose()
        self.assertTrue(0 <= random_num <= 2)

if __name__ == '__main__':
    unittest.main()
