# https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []


        def subInorderTraversal(el: Optional[TreeNode]) -> None:
            if el == None:
                return
            else:  
                subInorderTraversal(el.left)
                traversal.append(el.val)
                subInorderTraversal(el.right)
        

        subInorderTraversal(root)

        return traversal
