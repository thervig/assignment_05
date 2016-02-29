import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_permutations(self):
        self.assertEqual(len(analytics.permutations(99), 99)
        
    def test_critical_points(self):
        criticals = analytics.critical_points( 
