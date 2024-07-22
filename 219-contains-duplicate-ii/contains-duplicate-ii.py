class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        numbers_set=set()
        start=0
        for i in range(len(nums)):
            if i-start>k:
                numbers_set.remove(nums[start])
                start+=1

            if nums[i] in numbers_set:
                return True
            else:
                numbers_set.add(nums[i])

        return False
