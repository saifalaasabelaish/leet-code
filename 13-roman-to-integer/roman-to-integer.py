class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numbers={
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
        result=0
        length = len(s)
        i=0
        while i < length:
            if i + 1 < length and roman_numbers[s[i]] < roman_numbers[s[i + 1]]:
                result+=roman_numbers[s[i+1]]-roman_numbers[s[i]]
                i+=2
            else :
                result+=roman_numbers[s[i]]
                i+=1
        return result            

        
        



        
        