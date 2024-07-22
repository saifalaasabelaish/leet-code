class Solution(object):
    def groupAnagrams(self, strs):

        anagrams = {}
        
        for i in strs:
            anagram = ''.join(sorted(i))
            if anagram in anagrams:
                anagrams[anagram].append(i)
            else:
                anagrams[anagram] = []
                anagrams[anagram].append(i)
        anagrams_list = list(anagrams.values())
        return anagrams_list
