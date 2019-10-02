"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

## my first try. beat 91%. 
# 1->2->3->4->5->6
# 5->6->1->2->3->4
class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        if not head:
            return None
        # write your code here
        tail = head
        length = 0
        while tail.next:
            tail = tail.next
            length += 1
        tail.next = head

        node = head
        for _ in range(length - k % (length + 1)):
            node = node.next

        head = node.next
        node.next = None
        return head
