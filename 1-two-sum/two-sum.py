class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            sum=nums[i]
            for j in range(len(nums)):
                if (sum+nums[j]==target and i!=j):
                    return [i,j]
          