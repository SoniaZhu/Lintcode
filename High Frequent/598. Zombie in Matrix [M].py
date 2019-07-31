from collections import deque
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    queue.append((x, y))
                if grid[x][y] == 0:
                    count += 1

        day = -1
        while queue:
            day += 1
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                for (dx, dy) in DIRS:
                    newx = x + dx
                    newy = y + dy
                    if newx >= 0 and newx < len(grid) and newy >= 0 and newy < len(grid[0]) and grid[newx][newy] == 0:
                        queue.append((newx, newy))
                        grid[newx][newy] = 1
                        count -= 1

        if count != 0:
            return -1
        return day


from collections import deque
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = deque()
        count = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    queue.append((x, y, 0))
                if grid[x][y] == 0:
                    count += 1

        res = -1
        while queue:
            x, y, dep = queue.popleft()
            res = max(res, dep)
            for (dx, dy) in DIRS:
                newx = x + dx
                newy = y + dy
                if newx >= 0 and newx < len(grid) and newy >= 0 and newy < len(grid[0]) and grid[newx][newy] == 0:
                    queue.append((newx, newy, dep + 1))
                    grid[newx][newy] = 1
                    count -= 1

        if count != 0:
            return -1
        return res
