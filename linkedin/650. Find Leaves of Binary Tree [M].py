
## mine. second time. feel bad.

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
        tupleList = []
        self.dfs(root, tupleList)
        res = []
        for dep, val in tupleList:
            if dep >= len(res):
                res.append([])
            res[dep].append(val)
        return res

    def dfs(self, node, tupleList):
        if not node:
            return -1
        leftDep = self.dfs(node.left, tupleList)
        rightDep = self.dfs(node.right, tupleList)
        dep = max(leftDep, rightDep) + 1
        tupleList.append((dep, node.val))
        return dep

# better
class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    leaves = []
    # def __init__(self):
    #     self.leaves = []
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
