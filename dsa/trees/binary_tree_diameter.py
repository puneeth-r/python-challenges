"""Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them."""


from dsa.trees.utils import TreeNode
from typing import Optional


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = [0]

        def height(root):
            if root is None:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)
            diameter = left_height + right_height

            max_diameter[0] = max(max_diameter[0], diameter)
            return 1 + max(left_height, right_height)
        
        height(root)
        return max_diameter[0]
