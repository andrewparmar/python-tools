'''
Count triplets with sum smaller than a given value
'''

def three_sum(nums, target):

    count = 0
    triplets = []

    nums.sort()

    while i <= len(nums)-3:

        l = i + 1
        r = len(nums) - 1

        while l < r:
            three_sum = nums[i] + nums[l] + nums[r]
            if three_sum == target:
                triplets.append((nums[i], nums[l], nums[r]))
            if three_sum > target:
                r -= 1
            if three_sum < target:
                l += 1

        i += 1

    return triplets

def triplet_counter(nums, target):

    count = 0
    triplet = []

    
                









    return count