# https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for ch in ransomNote:
            if ch in dict:
                dict[ch] -= 1
            else:
                dict[ch] = -1
        for ch in magazine:
            if ch in dict:
                dict[ch] += 1
        for key in dict:
            if dict[key] < 0:
                return False
        return True
