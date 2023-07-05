# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_size = 0
        splitting = list()

        for num in nums:
            if not splitting:
                if num == 1:
                    splitting.append([True, 1])
                else:
                    splitting.append([False, 1])
            else:
                is_ones = splitting[-1][0]
                if is_ones:
                    if num == 1:
                        splitting[-1][1] += 1
                    else:
                        splitting.append([False, 1])
                else:
                    if num == 1:
                        splitting.append([True, 1])
                    else:
                        splitting[-1][1] += 1

        if len(splitting) == 1:
            if splitting[0][0]:
                return splitting[0][1] - 1
            else:
                return 0

        for i in range(len(splitting)):
            if splitting[i][0]:
                if splitting[i][1] > max_size:
                    max_size = splitting[i][1]
                if i < len(splitting) - 2 and splitting[i + 1][1] == 1:
                    cur_size = splitting[i][1] + splitting[i + 2][1]
                    if cur_size > max_size:
                        max_size = cur_size
            print(max_size)

        return max_size
