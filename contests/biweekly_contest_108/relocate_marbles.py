# https://leetcode.com/contest/biweekly-contest-108/problems/relocate-marbles/

class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        positions = dict()
        ans = list()
        n = len(nums)
        m = len(moveFrom)

        for i in range(0, n):
            if nums[i] in positions:
                positions[nums[i]] += 1
            else:
                positions[nums[i]] = 1

        for i in range(m):
            tmp = positions[moveFrom[i]]
            positions[moveFrom[i]] = 0
            if moveTo[i] in positions:
                positions[moveTo[i]] += tmp
            else:
                positions[moveTo[i]] = tmp

        for k in positions.keys():
            if positions[k] != 0:
                ans.append(k)

        return sorted(ans)
