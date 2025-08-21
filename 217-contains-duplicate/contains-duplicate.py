class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = set(nums)

        if len(nums)==len(x):
            return False
        else :
            return True