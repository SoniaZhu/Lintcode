## The best.
## My sol below. BAD: 1, not lazy (oop). 2, next should call has next.
class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.stack = nestedList[::-1]
        self.nextElement = None

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        if self.nextElement is None:
           self.hasNext()
        res, self.nextElement = self.nextElement, None
        return res

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        if self.nextElement:
            return True
        while self.stack:
            nextInteger = self.stack.pop()
            if nextInteger.isInteger():
                self.nextElement = nextInteger.getInteger()
                return True
            else:
                self.stack.extend(nextInteger.getList()[::-1])
        return False

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

## My sol. BAD: 1, not lazy (oop). 2, next should call has next.
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.flatList = []
        stack = nestedList[:]
        while stack:
            integer = stack.pop()
            if integer.isInteger():
                self.flatList.append(integer.getInteger())
            else:
                for child in integer.getList():
                    stack.append(child)
        self.flatList = self.flatList[::-1]
        self.index = -1

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.flatList[self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index + 1 < len(self.flatList)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
