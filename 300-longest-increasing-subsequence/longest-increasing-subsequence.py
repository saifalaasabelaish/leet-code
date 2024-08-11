class Solution(object):
    def lengthOfLIS(self, nums):
        if not nums :
            return 0
        if len(nums) == 0:
            return 0    

        n = len(nums)
        lists = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lists[i] = max(lists[i], lists[j] + 1)

        longest = 1
        for length in lists:
            longest = max(longest, length)

        return longest