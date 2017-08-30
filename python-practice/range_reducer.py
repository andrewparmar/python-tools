# BACKGROUND
# Sometimes items cannot be shipped to certain zip codes, and the rules for these restrictions are stored as a series of ranges of 5 digit codes.
# For example if the ranges are:
# [94133,94133] [94200,94299] [94600,94699]
# Then the item can be shipped to zip code 94199, 94300, and 65532, but cannot be shipped to 94133, 94650, 94230, 94600, or 94299.
# Any item might be restricted based on multiple sets of these ranges obtained from multiple sources.

# PROBLEM
# Given a collection of 5 digit ZIP code ranges (each range includes both their upper and lower bounds), provide an algorithm that produces the minimum number of ranges required to represent the same restrictions as the input .
import unittest

# implementation 1: without using sort
def range_reducer(list_of_ranges):
    reduced_list_ranges = []

    while (list_of_ranges):
        no_overlap_list = []
        if len(list_of_ranges) == 1:
            reduced_list_ranges.append(list_of_ranges[0])
            return reduced_list_ranges
        reduced_list_ranges.append(list_of_ranges[0])
        list_of_ranges.pop(0)
        low, high = reduced_list_ranges[-1][0], reduced_list_ranges[-1][1]
        for zip_range in list_of_ranges:
            if zip_range[0] in range(low, high + 1) or zip_range[1] in range(low, high + 1):
                reduced_list_ranges[-1][0] = min(reduced_list_ranges[-1][0], zip_range[0])
                reduced_list_ranges[-1][1] = max(reduced_list_ranges[-1][1], zip_range[1])
            else:
                no_overlap_list.append(zip_range)
        list_of_ranges = no_overlap_list

    return reduced_list_ranges


zip_list = [[94133, 94133],[94200, 94299],[94600, 94699],[94140, 94133]]
print(range_reducer(zip_list))