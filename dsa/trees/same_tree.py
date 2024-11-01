"""100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value."""

from typing import Optional
from dsa.trees.utils import TreeNode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        if not p and not q:
            return same
        
        if p and not q:
            return False
        
        if q and not p:
            return False
        
        if p.val != q.val:
            return False
        same = (self.isSameTree(p.left if p else None, q.left if q else None)) and (self.isSameTree(p.right if p else None, q.right if q else None))
        return same