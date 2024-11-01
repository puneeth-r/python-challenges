"""404. Sum of Left Leaves
Given the root of a binary tree, return the sum of all left leaves.
A leaf is a node with no children. A left leaf is a leaf that is the left child of another node."""

from typing import Optional
from dsa.trees.utils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def sum_left(root, curr_sum_left):
            if not root:
                return 0
            
            if not root.left and not root.right:
                return curr_sum_left
            curr_sum_left += sum_left(root.left, curr_sum_left)
        
        return sum_left(root, 0)


root:TreeNode{val: 3, left: TreeNode{val: 9, left: None, right: None}, right: TreeNode{val: 20, left: TreeNode{val: 15, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}}