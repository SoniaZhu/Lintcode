# not quite understand
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        suc = None
        while root:
            if root.val > p.val:
                suc = root
                root = root.left
            else:
                root = root.right
        return suc

class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        if root == None:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)

        left = self.inorderSuccessor(root.left, p)
        if left != None:
            return left
        else:
            return root

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        minLarge = [None]
        res = self.find(root, p, minLarge)
        if res and res.right:
            return self.getLeaf(res.right)
        else:
            return minLarge[0]

    def find(self, root, p, minLarge):
        if not root:
            return None
        if root.val == p.val:
            return root
        if root.val < p.val:
            return self.find(root.right, p, minLarge)
        if root.val > p.val:
            if not minLarge[0] or root.val < minLarge[0].val:
                minLarge[0] = root
            return self.find(root.left, p, minLarge)

    def getLeaf(self, root):
        if not root.left:
            return root
        return self.getLeaf(root.left)
