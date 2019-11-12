# 554
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        if not wall or not wall[0]:
            return 0
        freqMap = collections.Counter()
        maxCross = 0
        for row in wall:
            sum = 0
            for i in range(len(row) - 1):
                sum += row[i]
                freqMap[sum] += 1
                maxCross = max(maxCross, freqMap[sum])
        return len(wall) - maxCross

class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        if not heights:
            return 0
        # write your code here
        res = 0
        leftMax = 0
        rightMax = 0
        l = 0
        r = len(heights) - 1
        while l <= r:
            leftMax = max(heights[l], leftMax)
            rightMax = max(heights[r], rightMax)
            if leftMax < rightMax:
                res += leftMax - heights[l]
                l += 1
            else:
                res += rightMax - heights[r]
                r -= 1
        return res
