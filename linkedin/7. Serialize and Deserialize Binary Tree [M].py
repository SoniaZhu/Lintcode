# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

## correct answer. serialize is better but I like my deserialize better.
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)
            res.append(str(node.val) if node else "#");
        return " ".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        nodeData = [TreeNode(int(s)) if s != "#" else None for s in data.split()]
        root = nodeData[0]
        nodes = deque([root])
        dataIndex = 1
        while nodes:
            node = nodes.popleft()
            node.left = nodeData[dataIndex]
            node.right = nodeData[dataIndex + 1]
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            dataIndex += 2
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        nodeData = [TreeNode(int(s)) if s != "#" else None for s in data.split()]
        root = nodeData[0]
        nodes = [root]
        nodeIndex, dataIndex = 0, 1
        while nodeIndex < len(nodes):
            node = nodes[nodeIndex]
            node.left = nodeData[dataIndex]
            node.right = nodeData[dataIndex + 1]
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            nodeIndex += 1
            dataIndex += 2
        return root

## mine. did not serialize to a string.
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
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return ""
        res = []
        level = [root]
        while level:
            nextLevel = []
            for node in level:
                res.append(node.val if node else "#")
                if node:
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)
            if nextLevel.count(None) == len(nextLevel):
                break
            level = nextLevel
        return res

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if len(data) == 0:
            return None
        index = 1
        root = TreeNode(data[0])
        level = [root]
        while index < len(data):
            nextLevel = []
            for node in level:
                if data[index] != '#':
                    node.left = TreeNode(data[index])
                    nextLevel.append(node.left)
                index += 1

                if data[index] != '#':
                    node.right = TreeNode(data[index])
                    nextLevel.append(node.right)
                index += 1
            level = nextLevel
        return root

### fast but longer
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        res = [root.val]
        level = [root]
        while level:
            nextLevel = []
            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                    res.append(node.left.val)
                else:
                    res.append("#")
                if node.right:
                    nextLevel.append(node.right)
                    res.append(node.right.val)
                else:
                    res.append("#")
            if nextLevel.count(None) == len(nextLevel):
                break
            level = nextLevel
        return res
