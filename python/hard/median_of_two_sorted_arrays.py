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

 
# Use binary search
# explanation: https://redquark.org/leetcode/0004-median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        start = 0
        end = m

        while start <= end:
            partition_nums1 = (start + end) // 2
            partition_nums2 = (m + n + 1) // 2 - partition_nums1

            maxLeftNums1 = -sys.maxsize if partition_nums1 == 0 else nums1[partition_nums1 - 1]
            minRightNums1 = sys.maxsize if partition_nums1 == m else nums1[partition_nums1]

            maxLeftNums2 = -sys.maxsize if partition_nums2 == 0 else nums2[partition_nums2 - 1]
            minRightNums2 = sys.maxsize if partition_nums2 == n else nums2[partition_nums2]

            if maxLeftNums1 <= minRightNums2 and maxLeftNums2 <= minRightNums1:
                if (m + n) % 2 == 0:
                    return (max(maxLeftNums1, maxLeftNums2) + min(minRightNums1, minRightNums2)) / 2
                else:
                    return max(maxLeftNums1, maxLeftNums2)
            elif maxLeftNums1 > minRightNums2:
                end = partition_nums1 - 1
            else:
                start = partition_nums1 + 1
                
  
