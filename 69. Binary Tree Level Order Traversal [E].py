"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from queue import Queue
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        res = []
        if not root:
            return res
        queue = Queue()
        queue.put((root, 1))

        while not queue.empty():
            node, d = queue.get()
            if len(res) < d:
                res.append([node.val])
            else:
                res[-1].append(node.val)
            if node.left:
                queue.put((node.left, d + 1))
            if node.right:
                queue.put((node.right, d + 1))

        return res
