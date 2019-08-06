class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def __init__(self):
        self.leaves = []
    def findLeaves(self, root):
        # write your code here
        self.tree_height(root)
        return self.leaves

    def tree_height(self, root):
        if root == None:
            return -1
        left_height = self.tree_height(root.left)
        right_height = self.tree_height(root.right)
        height = 1 + max(left_height, right_height)
        if height >= len(self.leaves):
            self.leaves.append([])
        self.leaves[height].append(root.val)
        return height
    
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        nodeAndDept = []
        maxDept = self.helper(root, nodeAndDept)
        res = [[] for i in range(maxDept)]
        for val, dep in nodeAndDept:
            res[dep].append(val)
        return res

    def helper(self, root, lst):
        if not root:
            return -1
        res = max(self.helper(root.left, lst), self.helper(root.right, lst)) + 1
        lst.append((root.val, res))
        return res
