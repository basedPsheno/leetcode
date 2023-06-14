# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.same = True

        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]):
            if self.same:
                if (p and not q) or (q and not p):
                    self.same = False
                    return
                if not p and not q:
                    return
                if p.val != q.val:
                    self.same = False
                    return
                else:
                    dfs(p.left, q.left)
                    dfs(p.right, q.right)
            else:
                return
        
        dfs(p, q)


        return self.same
