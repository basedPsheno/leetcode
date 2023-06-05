# https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coords: List[List[int]]) -> bool:
        for i in range(2, len(coords)):
            if (coords[i][0] - coords[0][0]) * (coords[1][1] - coords[0][1]) != (coords[i][1] - coords[0][1]) * (coords[1][0] - coords[0][0]):
                return False
        return True
