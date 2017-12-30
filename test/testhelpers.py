from helpers import settings
import unittest

class TestMonty(unittest.TestCase):
    def test_trial(self):
        num_trial = 150
        settings.set_trial_number(num_trial) 
        self.assertEqual(settings.get_trial_number(), 150)

if __name__ == '__main__':
    unittest.main()
 
