class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        lists=['']*numRows
        current_row=0
        inc=1
        for i in s:
            lists[current_row]+=i
            if current_row==numRows-1:
                inc=-1
            elif current_row==0:
                inc=1
            current_row+=inc    
        return "".join(lists)            
        