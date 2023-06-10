# https://leetcode.com/contest/biweekly-contest-106/problems/check-if-the-number-is-fascinating/ 

class Solution:
    def isFascinating(self, n: int) -> bool:
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        saveN = n

        while n:
            if n % 10 in digits:
                digits.remove(n % 10)
            else:
                return False
            n //= 10

        n = saveN * 2
        while n:
            if n % 10 in digits:
                digits.remove(n % 10)
            else:
                return False
            n //= 10

        n = saveN * 3
        while n:
            if n % 10 in digits:
                digits.remove(n % 10)
            else:
                return False
            n //= 10

        return True
