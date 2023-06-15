# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        self.sums = {}
        max_sum = root.val

        def dfs(cur_level: int, node: Optional[TreeNode]):
            if node:
                if cur_level in self.sums:
                    self.sums[cur_level] += node.val
                else:
                    self.sums[cur_level] = node.val
                dfs(cur_level + 1, node.left)
                dfs(cur_level + 1, node.right)
            else:
                return
            
        dfs(1, root)

        for l, s in self.sums.items():
            if s > max_sum:
                max_sum = s
                level = l


        return level
