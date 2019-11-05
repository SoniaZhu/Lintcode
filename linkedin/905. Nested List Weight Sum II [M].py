from collections import deque
class Solution:
    """
    @param nestedList: a list of NestedInteger
    @return: the sum
    """
    def depthSumInverse(self, nestedList):
        # Write your code here.
        queue = deque(nestedList)
        presum = 0
        result = 0
        while queue:
            for _ in range(len(queue)):
                elem = queue.popleft()
                if elem.isInteger():
                    presum += elem.getInteger()
                else:
                    queue.extend(elem.getList())
            result += presum
        return result
                    
