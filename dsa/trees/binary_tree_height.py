"""Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node."""


# Tree
#         3
#    9         20
#          15      7

from dsa.trees.utils import TreeNode
from typing import Optional


class Solution:
    # time: O(n)
    # space: O(h)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not(root):
            return 0
        
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        return 1 + max(left_height, right_height)
    