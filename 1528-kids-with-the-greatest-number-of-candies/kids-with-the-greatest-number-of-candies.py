class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        length=len(candies)
        result=[]
        for i in range(length):
            if candies[i]+extraCandies>=max(candies):
                result.append(True)
            else: result.append(False)

        return result    


        