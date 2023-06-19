# https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_alt = 0
        cur_alt = 0

        for alt in gain:
            cur_alt += alt
            highest_alt = max(highest_alt, cur_alt)

        return highest_alt
