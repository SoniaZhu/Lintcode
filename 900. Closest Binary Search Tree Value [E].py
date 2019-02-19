"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
    	upper = root
        lower = root
        while root:
            if root.val > target:
                upper = root
                root = root.left
            elif root.val < target:
                lower = root
                root = root.right
            else:
                return root.val

        if abs(upper.val - target) > abs(lower.val - target):
            return lower.val
        return upper.val

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if not root:
            return -1
        current = root
        res = current.val
        while current:
            if abs(current.val - target) < abs(res - target):
                res = current.val
            if target > current.val:
                current = current.right
            else:
                current = current.left
        return res

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if not root:
            return -1
        if target > root.val:
            if not root.right:
                return root.val
            next = root.right
        else:
            if not root.left:
                return root.val
            next = root.left

        downMinVal = self.closestValue(next, target)
        if abs(root.val - target) < abs(downMinVal - target):
            return root.val
        else:
            return downMinVal

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if root is None:
            return None

        lower = self.get_lower_bound(root, target)
        upper = self.get_upper_bound(root, target)
        if lower is None:
            return upper.val
        if upper is None:
            return lower.val

        if target - lower.val < upper.val - target:
            return lower.val
        return upper.val

    def get_lower_bound(self, root, target):
        # get the largest node that < target
        if root is None:
            return None

        if target < root.val:
            return self.get_lower_bound(root.left, target)

        lower = self.get_lower_bound(root.right, target)
        return root if lower is None else lower

    def get_upper_bound(self, root, target):
        # get the smallest node that >= target
        if root is None:
            return None

        if target >= root.val:
            return self.get_upper_bound(root.right, target)

        upper = self.get_upper_bound(root.left, target)
        return root if upper is None else upper
