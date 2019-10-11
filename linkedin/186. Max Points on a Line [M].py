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

## second time doing it
class Solution:
    """
    @param points: an array of point
    @return: An integer
    """
    def maxPoints(self, points):
        # write your code here
        if not points:
            return 0
        res = 0
        for pt in points:
            slopeMap = dict()
            samePointCount = 0
            maxCount = 0
            sameXCount = 0
            for another in points:
                if another.x == pt.x and another.y == pt.y:
                    samePointCount += 1
                elif another.x == pt.x:
                    sameXCount += 1
                else:
                    slope = (pt.y - another.y) / (pt.x - another.x)
                    slopeMap[slope] = slopeMap.get(slope, 0) + 1
                    maxCount = max(maxCount, slopeMap[slope])
            res = max(res, samePointCount + max(maxCount, sameXCount))
        return res
