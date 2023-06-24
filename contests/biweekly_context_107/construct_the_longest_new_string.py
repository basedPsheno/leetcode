# https://leetcode.com/contest/biweekly-contest-107/problems/construct-the-longest-new-string/

import functools

class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        self.ans = 0

        @functools.cache
        def build_strings(cur_len: int, next: str, x: int, y: int, z: int):
            if cur_len > self.ans:
                self.ans = cur_len
            match next:
                case 'x':
                    if y > 0:
                        build_strings(cur_len + 2, 'y', x, y - 1, z)
                case 'y':
                    if x > 0:
                        build_strings(cur_len + 2, 'x', x - 1, y, z)
                    if z > 0:
                        build_strings(cur_len + 2, 'z', x, y, z - 1)
                case 'z':
                    if x > 0:
                        build_strings(cur_len + 2, 'x', x - 1, y, z)
                    if z > 0:
                        build_strings(cur_len + 2, 'z', x, y, z - 1)
                    
        
        build_strings(0, 'x', x, y, z)
        build_strings(0, 'y', x, y, z)
        build_strings(0, 'z', x, y, z)


        return self.ans
