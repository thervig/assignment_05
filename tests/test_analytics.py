import os
import sys
import unittest
sys.path.insert(0, os.path.abspath('..'))

from .. import analytics

class TestAnalytics(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_permutations(self):
        self.assertEqual(len(analytics.permutations(100), 100))
        
    def test_critical(self):
        critical_points = analytics.critical_points(analytics.permutations)
        self.assertEqual(min(analytics.permutations))
        self.assertEqual(max(analytics.permutations))
    
    def test_significance(self):
        critical = analytics.critical_points(analytics.permutations)
        self.assertTrue(critical_points[0] == min(analytics.permutations) and critical_points[1] == max(analytics.permutations))
