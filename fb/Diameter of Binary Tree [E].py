"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        # write your code here
        res = [0]
        self.helper(res, root)
        return res[0]

    def helper(self, res, root):
        if not root:
            return -1
        lh = self.helper(res, root.left)
        rh = self.helper(res, root.right)
        if lh + rh + 2 > res[0]:
            res[0] = lh + rh + 2
        return max(lh, rh) + 1
