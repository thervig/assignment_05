import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        pass
    
    def generate_random_test(self):
        self.assertEqual(len(utils.generate_random(100)), 100)
    
    def significant_distance_test(self):
        self.assertFalse(utils.significant_distance(9.9, 15, 10))
        self.assertTrue(utils.significant_distance(.05, .06, 1.0))
