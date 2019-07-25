class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        return self.getSum(nestedList, 1)

    def getSum(self, nestedList, depth):
        res = 0
        for elem in nestedList:
            if elem.isInteger():
                res += depth * elem.getInteger()
            else:
                res += self.getSum(elem.getList(), depth + 1)

        return res

class Solution(object):
    # @param {NestedInteger[]} nestedList a list of NestedInteger Object
    # @return {int} an integer
    def depthSum(self, nestedList):
        # Write your code here
        stack = []
        res = 0
        for n in nestedList:
            stack.append((n, 1))
        while stack:
            elem, depth = stack.pop()
            if elem.isInteger():
                res += elem.getInteger() * depth
            else:
                for next in elem.getList():
                    stack.append((next, depth + 1))
        return res
