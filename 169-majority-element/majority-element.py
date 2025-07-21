class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x={}
        for i in range (len(nums)):
             if nums[i] in x:
                x[nums[i]]=x[nums[i]]+1
             else :
                x[nums[i]]=0

    
        for key in x:
            if x.get(key)>=len(nums)/2:
                return key

