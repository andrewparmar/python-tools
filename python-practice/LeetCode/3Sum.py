def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solutions = []
        
        nums.sort()
        
        i = 0
        
        while i <= len(nums)-3:
            
            l = i + 1
            r = len(nums)-1
            
            while l<r:
                temp_sum = nums[l] + nums[r] + nums[i]
                # print "In while loop", temp_sum, solutions
                if temp_sum == 0:
                    solutions.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
                elif temp_sum > 0:
                    r -= 1
                elif temp_sum < 0:
                    l += 1
            # print solutions
            i += 1
        
        # print list(set(solutions))
        
        solution_set = []
        for item in list(set(solutions)):
            solution_set.append(list(item))         
        
        return solution_set
