# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        node = dummy = ListNode(-1)
        dummy.next = head
        while node.next and node.next.next:
            first = node.next
            second = node.next.next
            node.next = second
            first.next = second.next
            second.next = first
            node = first
        return dummy.next
            
