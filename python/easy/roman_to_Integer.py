# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        equals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        num = 0
        prev_digit = 0

        for digit in s[::-1]:
            if equals[digit] < prev_digit:
                num -= equals[digit]
            else:
                num += equals[digit]
            prev_digit = equals[digit]

        return num
