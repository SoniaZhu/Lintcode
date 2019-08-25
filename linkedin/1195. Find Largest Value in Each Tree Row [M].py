## one line don't know how to write
def largestValues(self, root):
        # write your code here
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max(node.val for node in row))
            row = [kid for node in row for kid in (node.left, node.right) if kid]
        return maxes

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque
class Solution:
    """
    @param root: a root of integer
    @return: return a list of integer
    """
    def largestValues(self, root):
        # write your code here
        res = []
        queue = deque([root])
        while queue:
            largest = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                largest = max(largest, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(largest)
        return res
