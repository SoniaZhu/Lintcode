"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
from heapq import heappush, heappop
class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        heap = []
        for point in points:
            heappush(heap, (-self.getDistance(point, origin), -point.x, -point.y))
            if len(heap) > k:
                heappop(heap)

        res = []
        for i in range(len(heap)):
            _, x, y = heappop(heap)
            res.append([-x, -y])
        res.reverse()
        return res

    def getDistance(self, point, origin):
        return (point.x - origin.x) ** 2 + (point.y - origin.y) ** 2
