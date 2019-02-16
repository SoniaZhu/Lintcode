"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from heapq import heappop, heappush
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        self.sequence = 0

        if not lists:
            return None
        heap = []
        for node in lists:
            if node:                ######### pay attention
                self.heappushNode(heap, node)
        current = dummy = ListNode(-1)

        while heap:
            node = heappop(heap)[2]
            current.next = ListNode(node.val)  # current.next = node
            current = current.next
            if node.next:            ######### pay attention
                self.heappushNode(heap, node.next)
        return dummy.next

    def heappushNode(self, heap, node):
        self.sequence += 1
        heappush(heap, (node.val, self.sequence, node))
