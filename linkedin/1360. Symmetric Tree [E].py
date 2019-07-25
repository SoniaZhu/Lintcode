"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself
    """
    def isSymmetric(self, root):
        # Write your code here
        return root is None or self.isMirror(root.left, root.right)

    def isMirror(self, node1, node2):
        if node1 is None or node2 is None:
            return node1 == node2
        if node1.val != node2.val:
            return False
        return self.isMirror(node1.left, node2.right) and self.isMirror(node1.right, node2.left)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the given tree
    @return: whether it is a mirror of itself
    """
    def isSymmetric(self, root):
        # Write your code here
        if not root:
            return True
        s = []
        s.append(root.left)
        s.append(root.right)
        while s:
            l = s.pop()
            r = s.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            s.append(l.left)
            s.append(r.right)
            s.append(l.right)
            s.append(r.left)
        return True
                  
