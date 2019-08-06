class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        self.sum = 0
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.right)
        self.sum += root.val
        root.val = self.sum
        self.dfs(root.left)

## this looks good but I dont understand my own codes!!!
class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        if root:
            self.helper(root, 0)
        return root

    def helper(self, root, sum):
        res = 0
        if root.right:
            res += self.helper(root.right, sum)
        res += root.val
        root.val = res + sum
        if root.left:
            res += self.helper(root.left, root.val)
        return res

class Solution:
    """
    @param root: the root of binary tree
    @return: the new root
    """
    def convertBST(self, root):
        # write your code here
        if root:
            self.helper(root, [0])
        return root

    def helper(self, root, last):
        if root.right:
            self.helper(root.right, last)
        root.val += last[0]
        last[0] = root.val
        if root.left:
            self.helper(root.left, last)
