# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: 
            return []
        
        if len(nums) == 1:
            return [f"{nums[0]}"]
        
        ranges = []
        a = b = 0
        for i in range(1, len(nums)):
            if nums[i] - nums[b] > 1:
                if nums[a] == nums[b]:
                    ranges.append(f"{nums[a]}")
                else:
                    ranges.append(f"{nums[a]}->{nums[b]}")
                a = b = i
            else:
                b = i

        if a == b:
            ranges.append(f"{nums[a]}")
        else:
            ranges.append(f"{nums[a]}->{nums[b]}")
            
        return ranges
