# https://leetcode.com/problems/valid-parentheses/

from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        valid = deque()
        valid.appendleft(s[0])

        for i in range(1, len(s)):
            if not valid:
                valid.appendleft(s[i])
            elif valid[0] in parentheses and parentheses[valid[0]] == s[i]:
                valid.popleft()
            else:
                valid.appendleft(s[i])
        
        return len(valid) == 0
