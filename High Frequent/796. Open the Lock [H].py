## Bidirectional BFS
## http://zxi.mytechroad.com/blog/searching/leetcode-752-open-the-lock/

from collections import deque
class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns
    """
    def openLock(self, deadends, target):
        # Write your code here
        dead = set(deadends)
        if "0000" in dead:
            return -1
        visited = set(["0000"])
        queue = deque(["0000"])
        move = -1
        while queue:
            move += 1
            for i in range(len(queue)):
                now = queue.popleft()
                if now == target:
                    return move
                for adjac in self.getAdjacent(now):
                    if adjac not in dead and adjac not in visited:
                        visited.add(adjac)
                        queue.append(adjac)
        return -1

    def getAdjacent(self, now):
        res = []
        for i in range(4):
            left, mid, right = now[:i], int(now[i]), now[i + 1:]
            for j in [(mid + 1) % 10, (mid - 1) % 10]:
                res.append(left + str(j) + right)
        return res
    ## huahua this is better https://www.youtube.com/watch?v=M7GgV6TJTdc


from collections import deque
class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns
    """
    def openLock(self, deadends, target):
        # Write your code here
        dead = set(deadends)
        if "0000" in dead:
            return -1
        DIREC = [(-1, 0, 0, 0), (1, 0, 0, 0), (0, -1, 0, 0), (0, 1, 0, 0), (0, 0, -1, 0), (0, 0, 1, 0), (0, 0, 0, -1), (0, 0, 0, 1)]
        visited = set(['0000'])
        queue = deque(['0000'])
        move = -1
        while queue:
            move += 1
            size = len(queue)
            for i in range(size):
                now = queue.popleft()
                if now == target:
                    return move
                for dx, dy, dp, dq in DIREC:
                    nx = (int(now[0]) + dx) % 10
                    ny = (int(now[1]) + dy) % 10
                    np = (int(now[2]) + dp) % 10
                    nq = (int(now[3]) + dq) % 10
                    next = str(nx) + str(ny) + str(np) + str(nq)
                    if next not in visited and next not in dead:
                        queue.append(next)
                        visited.add(next)
        return -1
