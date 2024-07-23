class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set=set(nums)
        max_length=0
        for i in nums:
            if i-1 not in nums_set:
                next_num=i+1
                length=1
                while next_num in nums_set:
                    length+=1
                    next_num+=1
                max_length=max(max_length,length)
        return max_length       
        