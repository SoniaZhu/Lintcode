
## huahua - hard to avoid mistakes. works on leetcode but not lintcode.
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):   # not len - 1. for single input
            p1 = points[i]
            samePoints = 1
            maxPoints = 0
            hash = dict()
            for j in range(i + 1, len(points)):
                p2 = points[j]
                if p1 == p2:
                    samePoints += 1
                else:
                    slope = self._getSlope(p1, p2)
                    hash[slope] = hash.get(slope, 0) + 1
                    maxPoints = max(maxPoints, hash[slope])
            res = max(res, maxPoints + samePoints)
        return res

    def _getSlope(self, p1, p2):
        dy = p1[1] - p2[1]
        dx = p1[0] - p2[0]
        if dy == 0:
            return (p1[0], 0)       # can be any. or (p1[1], 0), or (0, p1[1])
        if dx == 0:
            return (0, p1[0])       # can be any
        gcd = self._gcd(dy, dx)
        return (dy / gcd, dx / gcd)

    def _gcd(self, p1, p2):
        if p1 == 0:
            return p2
        return self._gcd(p2 % p1, p1)
