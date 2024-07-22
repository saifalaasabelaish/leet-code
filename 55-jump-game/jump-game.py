class Solution(object):
    def canJump(self, nums):
        max_jump = nums[0]
        target = len(nums) - 1

        if max_jump >= target:
            return True

        for i in range(1, len(nums)):
            if i > max_jump:
                return False
            max_jump = max(max_jump, nums[i] + i)
            if max_jump >= target:
                return True
            
        return False
