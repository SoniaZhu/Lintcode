## 1. small to large  2. [a,b] [a, b=c*d]
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        res = []
        self.helper(res, [], n)
        return res

    def helper(self, res, path, reminder):
        if path:
            path.append(reminder)
            res.append(path[:])
            path.pop()
        start = path[-1] if path else 2
        for i in range(start, int(math.sqrt(reminder)) + 1):
            if reminder % i == 0:
                path.append(i)
                self.helper(res, path, reminder // i)
                path.pop()

class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        res = []
        self.helper(n, [], res)
        return res

    def helper(self, n, temp, res):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                temp1 = list(temp)
                if len(temp1) >= 1 and i < temp1[-1]:
                    continue
                temp1.append(i)
                temp2 = list(temp1)
                temp1.append(n // i)
                res.append(temp1)
                self.helper(n // i, temp2, res)
