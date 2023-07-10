# https://leetcode.com/problems/minimum-depth-of-binary-tree/ 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        queue = collections.deque()
        queue.appendleft((root, 1))

        while queue:
            cur_node, dep = queue.popleft()
            if not cur_node.left and not cur_node.right:
                return dep
            if cur_node.left:
                queue.append((cur_node.left, dep + 1))
            if cur_node.right:
                queue.append((cur_node.right, dep + 1))
