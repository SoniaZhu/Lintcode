"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from heapq import heappush, heappop
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        heap = []
        sequence = 0
        for node in lists:
            sequence = self.push(heap, node, sequence)

        dummy = previous = ListNode(-1)
        while heap:
            _, _, node = heappop(heap)
            previous.next = node
            previous = node
            sequence = self.push(heap, node.next, sequence)
        return dummy.next

    def push(self, heap, node, sequence):
        if node:
            heappush(heap, (node.val, sequence + 1, node))
            return sequence + 1
        else:
            return sequence

from heapq import heappop, heappush
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        heap = []
        counter = 0
        for node in lists:
            if node:
                heappush(heap, (node.val, counter, node))
                counter += 1
        if not heap:
            return None
        root = prev = heappop(heap)[2]
        if root.next:
            heappush(heap, (root.next.val, counter, root.next))
            counter += 1

        while heap:
            current = heappop(heap)[2]
            prev.next = current
            if current.next:
                heappush(heap, (current.next.val, counter, current.next))
                counter += 1
            prev = current

        return root

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
