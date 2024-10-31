import logging

logging.basicConfig(level=logging.DEBUG, format = "%(message)s")


#        1
#    2       3   
#  4   5   10
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value=value
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.value)

A=TreeNode(1)
B=TreeNode(2)
C=TreeNode(3)
D=TreeNode(4)
E=TreeNode(5)
F=TreeNode(10)
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
def in_order(node):
    print(f"node1:{node}")
    if not node:
        return
    
    in_order(node.left)
    logging.info(node)
    in_order(node.right)
    print(f"node2:{node}")

in_order(A)
