class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        
        while matrix:
            res += matrix.pop(0)
            
            if not matrix:
                break
            
            for row in matrix:
                if row: 
                    res.append(row.pop())
            
            if not matrix:
                break
            
            if matrix[-1]:
                res += matrix.pop()[::-1]
            
            if not matrix:
                break
            
            for row in matrix[::-1]:
                if row:
                    res.append(row.pop(0))
        
        return res
