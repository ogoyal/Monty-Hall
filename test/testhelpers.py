from helpers import settings
import unittest

class TestMonty(unittest.TestCase):
    def test_trial(self):
        num_trial = 1000
        settings.set_trial_number(num_trial) 
        self.assertEqual(settings.get_trial_number(), 1000)

    def test_sections(self):
        num_sections = 100
        settings.set_sections(num_sections)
        self.assertEqual(settings.get_sections(), 100)

if __name__ == '__main__':
    unittest.main()
 
