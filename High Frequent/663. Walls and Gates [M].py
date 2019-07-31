from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        rs = len(rooms)
        cs = len(rooms[0])

        queue = deque()
        for x in range(rs):
            for y in range(cs):
                if rooms[x][y] == 0:
                    queue.append((x, y))

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            cx, cy = queue.popleft()
            for dx, dy in dirs:
                newx = cx + dx
                newy = cy + dy
                if newx >= 0 and newx < rs and newy >= 0 and newy < cs and rooms[newx][newy] == 2147483647:
                    queue.append((newx, newy))
                    rooms[newx][newy] = rooms[cx][cy] + 1
        return rooms



class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        for x in range(len(rooms)):
            for y in range(len(rooms[0])):
                if rooms[x][y] == 0:
                    Solution.propagateAround(rooms, x, y)
        return rooms

    @staticmethod
    def propagateAround(rooms, x, y):
        value = rooms[x][y]
        if y - 1 >= 0:
            Solution.calculateDist(rooms, x, y - 1, value)
        if y + 1 < len(rooms[0]):
            Solution.calculateDist(rooms, x, y + 1, value)
        if x - 1 >= 0:
            Solution.calculateDist(rooms, x - 1, y, value)
        if x + 1 < len(rooms):
            Solution.calculateDist(rooms, x + 1, y, value)

    @staticmethod
    def calculateDist(rooms, nextX, nextY, centerD):
        nextD = rooms[nextX][nextY]
        if nextD > 0 and nextD > centerD + 1:
            rooms[nextX][nextY] = centerD + 1
            Solution.propagateAround(rooms, nextX, nextY)
