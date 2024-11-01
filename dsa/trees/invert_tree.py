"""226. Invert Binary Tree
Given the root of a binary tree, invert the tree, and return its root."""
from typing import Optional
from dsa.trees.utils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.value = value
#         self.left = left
#         self.right = right
class Solution:
    # time: O(n)
    # space: O(h)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root