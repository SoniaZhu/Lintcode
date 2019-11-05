# 1 -> 2 -> 3 -> 2       2321
# 4 -> 5 -> 6            654  ->

# 9   9  9 9 9 9
# 9
class ListNode:
    def __init__(self, val, next = None):
        self.val = eval
        self.next = next

def getSum(node1, node2):

    carry = 0
    dummy = node = ListNode(-1)
    while node1 and node2:
        sum = carry
        sum += node1.val if node1 else 0
        sum += node2.val if node2 else 0
        node.next = ListNode(sum % 10)
        carry = sum // 10
        node = node.next
        node1 = node1.next
        node2 = node2.next

    if carry != 0:
        node.next = ListNode(carry)
    return dummy.next

## 1 000000000000000000000->2     0
##                                2
