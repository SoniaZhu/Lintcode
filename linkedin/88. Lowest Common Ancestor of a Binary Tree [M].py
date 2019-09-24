"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# A & 下面有B => A
# B & 下面有A => B
# A & 下面啥都没有 => A
# B & 下面啥都有 => B
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        if not root:
            return None
        # A & 下面有B => A
        # B & 下面有A => B
        # A & 下面啥都没有 => A
        # B & 下面啥都有 => B
        if root.val == A.val or root.val == B.val:
            return root

        leftRes = self.lowestCommonAncestor(root.left, A, B)
        rightRes = self.lowestCommonAncestor(root.right, A, B)
        if leftRes and rightRes:
            return root
        if leftRes:
            return leftRes
        return rightRes
