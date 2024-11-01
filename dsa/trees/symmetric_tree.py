"""101. Symmetric Tree
Easy
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center)."""

from dsa.trees.utils import TreeNode
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.value = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def same(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
            
            if root1.value != root2.value:
                return False

            return same(root1.left, root2.right) and same(root1.right, root2.left)