#!/bin/bash/python

import unittest

import MathFunctions

class TestMath(unittest.TestCase):
	# Test areaCircle()
	def test_areaCircle_for_10radius(self):
		# Capture results of function
		results = MathFunctions.areaCircle(10)
		# Check for expected output
		expected = 314.1592653589793
		self.assertEqual(expected, results)
	def test_areaCircle_for_1radius(self):
		# Capture results of function
		results = MathFunctions.areaCircle(1)
		# Check for expected output
		expected = 3.141592653589793
		self.assertEqual(expected, results)


# Run the Tests
if __name__ == "__main__":
	unittest.main()