class Solution:
    """
    @param root: the root
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """
    def findSecondMinimumValue(self, root):
        # Write your code here
        if not root or not root.left:
            return -1
        left = root.left.val
        if left == root.val:
            left = self.findSecondMinimumValue(root.left)

        right = root.right.val
        if right == root.val:
            right = self.findSecondMinimumValue(root.right)

        if left == -1:
            return right
        if right == -1:
            return left
        return min(left, right)

## my second version
class Solution:
    """
    @param root: the root
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """
    def findSecondMinimumValue(self, root):
        # Write your code here
        if not root.left:
            return -1
        if min(root.left.val, root.right.val) > root.val:
            return min(root.left.val, root.right.val)
        if max(root.left.val, root.right.val) > root.val:
            return max(root.left.val, root.right.val)
        return min(self.findSecondMinimumValue(root.left), self.findSecondMinimumValue(root.right))

## my first version
class Solution:
    """
    @param root: the root
    @return: the second minimum value in the set made of all the nodes' value in the whole tree
    """
    def findSecondMinimumValue(self, root):
        # Write your code here
        if not root:
            return -1
        level = [root]
        minimum = float('inf')
        while len(level) > 0 and minimum == float('inf'):
            nextLevel = []
            for node in level:
                if node.val < minimum and node.val > root.val:
                    minimum = node.val
                if node.left:
                    nextLevel.append(node.left)
                    nextLevel.append(node.right)
            level = nextLevel
        if minimum != float('inf'):
            return minimum
        return -1
