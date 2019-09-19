
## mine first version.
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        carry, currentNodeRes = self.plusOneHelper(head)
        if carry == 0:
            return currentNodeRes
        else:
            newHead = ListNode(1)
            newHead.next = currentNodeRes
            return newHead

    def plusOneHelper(self, node):
        if not node:
            return (1, node)
        carry, nextNodeRes = self.plusOneHelper(node.next)

        if carry == 1 and node.val == 9:
            currentNodeRes = ListNode(0)
            carry = 1
        else:
            currentNodeRes = ListNode(node.val + carry)
            carry = 0
        currentNodeRes.next = nextNodeRes
        return (carry, currentNodeRes)
