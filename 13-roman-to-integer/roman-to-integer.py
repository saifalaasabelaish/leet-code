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
        i=0
        output = 0
        for i in range(len(s)-1):
            if roman_numbers[s[i]] < roman_numbers[s[i+1]]:
                result -= roman_numbers[s[i]]
            else:
                result += roman_numbers[s[i]]
        
        return result+roman_numbers[s[-1]]           

        
        



        
        