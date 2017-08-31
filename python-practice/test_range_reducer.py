import unittest

import range_reducer

class Test_range_reducer(unittest.TestCase):

	def setUp(self):
		self.SET1 = [[94133, 94133],[94200, 94299],[94600, 94699],[94120, 94133]]
		self.SET2 = [[94133, 94299]]
		self.SET3 = []
		self.SET4 = [[94133, 94133],[94133, 94133]]
	
	def test_range_reducer(self):
		self.assertEquals(range_reducer.zip_range_reducer(self.SET1), [[94120, 94133], [94200, 94299], [94600, 94699]])
		self.assertEquals(range_reducer.zip_range_reducer(self.SET2), [[94133, 94299]])
		self.assertEquals(range_reducer.zip_range_reducer(self.SET2), [[94133, 94299]])


	def test_range_reducer_exception(self):
		self.assertRaises(Exception, range_reducer.zip_range_reducer, self.SET3)


if __name__ == "__main__":
	unittest.main()