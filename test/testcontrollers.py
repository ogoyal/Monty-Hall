from controllers import monty
from helpers import settings
import unittest

class TestController(unittest.TestCase):

    '''
    Setup Tests. This is called before every test.
    '''
    def setUp(self):
        settings.set_trial_number(10000)
        settings.set_sections(150)
        monty.__init__()

    def test_choose(self):
        random_num = monty.choose()
        self.assertTrue(0 <= random_num <= 2)

    '''
    Support User changes the answer after host tells him where one of the sheep is. Probability should be around 66%.
    '''
    def test_change_choice(self):
        prob = monty.change_choice()
        self.assertTrue(0.65 <= prob[-1] <= 0.68)

    '''
    Suppose User sticks with his answer after host tells him where one of the sheep is. Probability should be around 33%.
    '''
    def test_same_choice(self):
        prob = monty.same_choice()
        self.assertTrue(0.32 <= prob[-1] <= 0.34)


if __name__ == '__main__':
    unittest.main()
