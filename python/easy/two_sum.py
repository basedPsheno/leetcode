# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pref = dict()

        for i in range(len(nums)):
            if target - nums[i] in pref:
                return [i, pref[target - nums[i]]]
            pref[nums[i]] = i
