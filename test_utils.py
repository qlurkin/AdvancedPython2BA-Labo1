# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
	def test_fact(self):
		self.assertEqual(utils.fact(5), 120)
		self.assertEqual(utils.fact(0), 1)
		with self.assertRaises(ValueError):
			utils.fact(-1)
	
	def test_roots(self):
		self.assertEqual(utils.roots(1,0,0), (0,))
		self.assertEqual(utils.roots(1,0,-1), (1,-1))
		self.assertEqual(utils.roots(1,0,1), tuple())
	
	def test_integrate(self):
		self.assertEqual(utils.integrate('1', 0, 1), 1)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
	runner = unittest.TextTestRunner()
	exit(not runner.run(suite).wasSuccessful())