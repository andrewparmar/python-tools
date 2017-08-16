def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n in nums:
            delta = target-n
            n_index = nums.index(n)
            delta_index = nums.index(delta)
            if delta in nums:
                if delta != n:             
                    return [n_index, delta_index]
                elif delta == n:
                    try:                  
                        delta_index = nums.index(delta,n_index+1)
                        # print(n_index)
                        # print()
                        return [n_index, delta_index]

nums = [3,2,4]
target = 6

print(twoSum(nums, target))



# for n in nums:
#             delta = target-n
#             n_index = nums.index(n)
#             delta_index = nums.index(delta)
#             if delta in nums and delta != n:             
#                 return [n_index, delta_index]

def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for n in nums:
            delta = target-n        
            if delta in nums:
                n_index = nums.index(n)
                delta_index = nums.index(delta)
                if delta != n:             
                    return [n_index, delta_index]
                elif delta == n and n_index < len(nums)-1:
                    try:                  
                        delta_index = nums.index(delta,n_index+1)
                        return [n_index, delta_index]
                    except:
                        pass

            table = {}

            for n in nums:
                if target-n in x:
                    return table[x]