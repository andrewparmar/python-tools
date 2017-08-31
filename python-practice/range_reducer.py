#!usr/bin/python

'''
BACKGROUND
Sometimes items cannot be shipped to certain zip codes, and the rules 
for these restrictions are stored as a series of ranges of 5 digit codes.
For example if the ranges are:
[94133,94133] [94200,94299] [94600,94699]
Then the item can be shipped to zip code 94199, 94300, and 65532, but
cannot be shipped to 94133, 94650, 94230, 94600, or 94299.
Any item might be restricted based on multiple sets of these ranges
obtained from multiple sources.

PROBLEM
Given a collection of 5 digit ZIP code ranges (each range includes both
their upper and lower bounds),
provide an algorithm that produces the minimum number of ranges required
to represent the same restrictions as the input.
'''

__author__ = "Andrew Parmar"
__email__ = "andrew.parmar@gmail.com"


import unittest


# Implementation
def zip_range_reducer(zip_range_list):

    if not zip_range_list:
        raise Exception("Empty list of ranges provided!")

    reduced_zip_ranges = []

    zip_range_list.sort()

    while (zip_range_list):
        no_overlap_ranges = []
        reduced_zip_ranges.append(zip_range_list[0])
        if len(zip_range_list) == 1:
            return reduced_zip_ranges
        zip_range_list.pop(0)
        for zip_range in zip_range_list:
            low, high = reduced_zip_ranges[-1][0], reduced_zip_ranges[-1][1]
            range_check = range(low-1, high+2)
            if zip_range[0] in range_check or zip_range[1] in range_check:
                reduced_zip_ranges[-1][0] = min(reduced_zip_ranges[-1][0], zip_range[0])
                reduced_zip_ranges[-1][1] = max(reduced_zip_ranges[-1][1], zip_range[1])
            else:
                no_overlap_ranges.append(zip_range)
        zip_range_list = no_overlap_ranges

    return reduced_zip_ranges


# Testing
class Test_Range_Reducer(unittest.TestCase):

    def setUp(self):
        self.set1 = [[94133, 94133], [94200, 94299],[94600, 94699], [94120, 94133]]
        self.set2 = [[94133, 94299], [94133, 94299]]
        self.set3 = [[14,17], [4,7], [2,5], [10,12] , [15,16], [4,9], [11,13]]
        self.set4 = [[12345, 123457]]
        self.empty_set = []
        

    def test_range_reducer(self):
        self.assertEquals(zip_range_reducer(self.set1), [[94120, 94133],[94200, 94299],[94600, 94699]])
        self.assertEquals(zip_range_reducer(self.set2), [[94133, 94299]])
        self.assertEquals(zip_range_reducer(self.set2), [[94133, 94299]])
        self.assertEquals(zip_range_reducer(self.set3), [[2,17]])
        self.assertEquals(zip_range_reducer(self.set4), [[12345, 123457]])

    def test_range_reducer_exception(self):
        self.assertRaises(Exception, zip_range_reducer, self.empty_set)


if __name__ == "__main__":
    unittest.main()