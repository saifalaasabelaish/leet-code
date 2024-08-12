class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        prev1 = nums[0]  
        prev2 = max(nums[0], nums[1])  
        
        for i in range(2, n):
            current = max(prev2, prev1 + nums[i])
            prev1 = prev2  
            prev2 = current  
        
        return prev2
