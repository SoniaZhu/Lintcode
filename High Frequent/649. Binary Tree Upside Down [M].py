class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        node, parent, right = root, None, None
        while node:
            left = node.left
            node.left = right
            right = node.right
            node.right = parent
            parent = node
            node = left
        return parent

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        if not root:
            return None
        if not root.left:
            return root
        res = self.upsideDownBinaryTree(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None
        return res
