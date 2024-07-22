class Solution(object):
    def hIndex(self, citations):
        
        citations.sort()
        n = len(citations)
        
        for i in range(n):
            if n - i <= citations[i]:
                return n - i
        
        return 0