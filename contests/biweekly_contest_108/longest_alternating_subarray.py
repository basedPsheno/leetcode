# https://leetcode.com/contest/biweekly-contest-108/problems/longest-alternating-subarray/

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        cur_len = 0
        turn = 1

        for i in range(1, n):
            if nums[i] - nums[i - 1] == turn:
                if cur_len == 0:
                    cur_len = 2
                else:
                    cur_len += 1
                turn *= -1
            else:
                if nums[i] - nums[i - 1] == 1:
                    cur_len = 2
                    turn = -1
                else:
                    cur_len = 0
                    turn = 1
            if cur_len > ans and cur_len != 0:
                ans = cur_len

        return ans
