# https://leetcode.com/problems/k-radius-subarray-averages/

class Solution:        
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        mod = 2 * k + 1
        if n < mod:
            return [-1] * n
        avgs = [-1] * k + [0] * (n - 2 * k) + [-1] * k
        cur_sum = sum(nums[:mod])
        
        for i in range(n - 2 * k - 1):
            avgs[k + i] = cur_sum // mod
            cur_sum -= nums[i]
            cur_sum += nums[mod + i]

        avgs[n - k - 1] = cur_sum // mod

        return avgs
