# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            len_x = -1
            new_x = x
            while new_x:
                new_x = new_x // 10
                len_x += 1
            while x and len_x >= 0:
                if x // (10 ** len_x) != x % 10:
                    return False
                x = x % (10 ** len_x)
                x = x // 10
                len_x -= 2
            return True
