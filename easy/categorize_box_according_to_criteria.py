# https://leetcode.com/problems/categorize-box-according-to-criteria/

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:

        code = [False] * 2

        if (length >= 10000 or width >= 10000 or height >= 10000) or (length * width * height >= 1000000000):
            code[0] = True
        if mass >= 100:
            code[1] = True
        
        if code[0] == code[1] == True:
            return "Both"
        if code[0] == code[1] == False:
            return "Neither"
        if code[0] == True and code[1] == False:
            return "Bulky"
        if code[0] == False and code[1] == True:
            return "Heavy"
