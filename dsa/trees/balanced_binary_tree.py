"""Given a binary tree, determine if it is height balanced.
A balanced binary tree is defined as a binary tree where the height of left subtree and 
right sub-tree of every node differ in height no more than 1"""

# Tree
#         3
#    9         20
#          15      7
from dsa.trees.utils import TreeNode
from typing import Optional



class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:  
        balanced = [True]             
        
        def height(root):
            if not root:
                return 0
            left_height = height(root.left)
            if balanced[0] is False:
                return 0
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(left_height, right_height)
        
        height(root)
        return balanced[0]
    



root = [3,9,20,None,None,15,7]  
A=TreeNode(3)
B=TreeNode(9)
C=TreeNode(20)
D=TreeNode(15)
E=TreeNode(7)
A.left = B
A.right= C
C.left = D
C.right = E

print(Solution().isBalanced(root=A))
