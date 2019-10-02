"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        lengA, lengB = 0, 0
        currentA, currentB = headA, headB
        while currentA:
            lengA += 1
            currentA = currentA.next
        while currentB:
            lengB += 1
            currentB = currentB.next

        shorter = headA if lengA < lengB else headB
        longer = headB if lengA < lengB else headA

        for _ in range(abs(lengA - lengB)):
            longer = longer.next
        while shorter:
            if shorter.val == longer.val:    # wrong
                return shorter
            shorter = shorter.next
            longer = longer.next
        return None

####################
# line 31
        while shorter != longer:    # while short is not longer:
            shorter = shorter.next
            longer = longer.next
        return shorter
