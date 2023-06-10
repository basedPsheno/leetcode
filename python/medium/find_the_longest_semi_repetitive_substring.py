# https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

'''
Intuition

If you mentally divide a string into substrings that do not contain
repeating elements, it becomes clear that you can get the string
you are looking for by adding the two neighboring strings.

Example:
211162506623
21|1|162506|623

We only need to return the length of the substring, so we don't need 
indices. Element counting is easy to implement, and we just store 
the lengths in the list. By going through the list and adding all 
neighboring values, we can find the maximum.
'''
class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        res = 0
        tab = [1]
        
        for i in range(1,len(s)):
            if s[i] == s[i - 1]:
                tab.append(1)
            else:
                tab[-1] = tab[-1] + 1
                
        for j in range(1, len(tab)):
            res = max(res, tab[j] + tab[j - 1])
        
        return max(res, tab[0])
