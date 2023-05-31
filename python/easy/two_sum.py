# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        match = {}

        for i in range(len(nums)):
            match[nums[i]] = i
        
        for i in range(len(nums)):
            compl = target - nums[i]
            if compl in match and match[compl] != i:
                return [i, match[compl]]
