"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given tree
    @return: the binary tree in an m*n 2D string array
    """
    def printTree(self, root):
        # Write your code here
        m, n = self.getTemplate(root)
        res = [['' for _ in range(n)] for _ in range(m)]
        self.update(root, 0, n - 1, 0, res)
        return res

    def update(self, node, left, right, level, res):
        if not node:
            return
        mid = (left + right) // 2
        res[level][mid] = str(node.val)
        self.update(node.left, left, mid - 1, level + 1, res)
        self.update(node.right, mid + 1, right, level + 1, res)

    def getTemplate(self, root):
        m = self.getMaxHeight(root)
        return (m, 2 ** m - 1)

    def getTemplate2(self, root):
        m = self.getMaxHeight(root)
        n = 0
        for i in range(m):
            n = n * 2 + 1
        return (m, n)

    def getMaxHeight(self, node):
        if not node:
            return 0
        return 1 + max(self.getMaxHeight(node.left), self.getMaxHeight(node.right))
