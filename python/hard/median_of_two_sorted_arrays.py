# https://leetcode.com/problems/median-of-two-sorted-arrays/

# no run time complexity O(log(n+m))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)

        n = len(merged)
        if n % 2 == 0:
            mid = n // 2
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            mid = n // 2
            return merged[mid]
