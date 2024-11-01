"""112. Path Sum
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children."""

from typing import Optional
from dsa.trees.utils import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time : O(n)
    # space: O(h)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(root, curr_sum):
            if not root:
                return False
            
            curr_sum += root.val

            if not root.left and not root.right:
                return curr_sum == targetSum
            
            return has_sum(root.left, curr_sum) or has_sum(root.right, curr_sum)
        
        return has_sum(root, 0)