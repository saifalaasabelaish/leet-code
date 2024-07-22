class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #if nums[0]>=len(nums)-1:
         #   return 1

        jumps=0
        maximum_jump=0
        current_index=0
        for i in range (len(nums)-1):
            maximum_jump=(max(maximum_jump,nums[i]+i))
            if maximum_jump>=len(nums)-1:
                jumps+=1
                break
            if i==current_index:
                jumps+=1
                current_index=maximum_jump
        return jumps                

        