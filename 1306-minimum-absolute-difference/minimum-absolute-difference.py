class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        min_diff=float('inf')
        arr.sort()
        for i in range(1,len(arr)):
            min_diff=min(min_diff,arr[i]-arr[i-1])

        results=[]
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1]==min_diff:
                results.append([arr[i-1],arr[i]])

        return results        