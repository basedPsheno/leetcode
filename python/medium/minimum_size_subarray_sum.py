# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        ans = 0
        n = len(nums)

        left = 0
        cur_sum = 0
        cur_len = 0

        for right in range(n):
            cur_sum += nums[right]
            cur_len += 1

            if cur_sum >= target:
                while cur_sum >= target:
                    cur_sum -= nums[left]
                    left += 1
                    cur_len -= 1
                cur_len += 1
                left -= 1
                cur_sum += nums[left]

                if ans == 0:
                    ans = cur_len
                if cur_len < ans:
                    ans = cur_len

        return ans
