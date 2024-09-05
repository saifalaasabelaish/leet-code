class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums:  
                complement_index = nums.index(complement)
                if complement_index != i:
                    return [i, complement_index]
