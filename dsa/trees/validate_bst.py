from typing import Optional
from dsa.trees.utils import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def is_bst(node, minn, maxx):
            if not node:
                return True
            
            if node.val <= minn or node.val >= maxx:
                return False
            
            return is_bst(node=node.left, maxx=node.val, minn=minn) and is_bst(node=node.right, maxx=maxx, minn=node.val)

        return is_bst(node=root, minn=float("-inf"), maxx=float("inf"))



                
            

        