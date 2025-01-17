"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):
        # write your code here
        carry = 0
        dummy = node = ListNode(-1)
        while l1 or l2:
            sum = l1.val if l1 else 0
            sum += l2.val if l2 else 0
            sum += carry
            node.next = ListNode(sum % 10)
            carry = sum // 10
            node = node.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry != 0:
            node.next = ListNode(carry)
        return dummy.next
