class Solution(object):
    def combinationSum4(self, nums, target):
        if not nums or all(num > target for num in nums):
            return 0
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums: 
                pre = i - num
                if pre >= 0:
                    dp[i] += dp[pre]
        return dp[target]    
            
        