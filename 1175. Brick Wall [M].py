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
