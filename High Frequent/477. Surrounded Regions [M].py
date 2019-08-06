## 这道题还是看答案吧
## 这道题还是看答案吧
class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
            # write your code here
            if len(board) == 0:
                return board
            n, m = len(board), len(board[0])
            startNodes = []
            for x in range(n):
                for y in range(m):
                    if (x == 0 or x == n-1 or y == 0 or y == m-1) and board[x][y] == 'O':
                        startNodes.append((x, y))

            self.bfs(board, startNodes)
            board[:] = [['XO'[c == 'W'] for c in row] for row in board]

    def bfs(self, board, startNodes):
        queue = deque(startNodes)
        while queue:
            (x, y) = queue.popleft()
            if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] == 'O':
                board[x][y] = 'W'
                queue += (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)


class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        if len(board) == 0:
            return board
        self.rs, self.cs = len(board), len(board[0])
        visited = set()
        for x in range(self.rs):
            for y in range(self.cs):
                if board[x][y] == 'O' and (x, y) not in visited and self.isRegion(x, y, board, visited):
                    print ("Aaa")
                    self.change(x, y, board)
        return board

    def isRegion(self, x, y, board, visited):
        DIRS = [(0,1),(0,-1),(-1,0),(1,0)]
        visited.add((x, y))
        res = True
        for dx, dy in DIRS:
            newx = x + dx
            newy = y + dy
            if newx < 0 or newy < 0 or newx >= len(board) or newy >= len(board[0]):
                res = False
                continue
            if board[newx][newy] != 'X' and (newx, newy) not in visited:
                if not self.isRegion(newx, newy, board, visited):
                    res = False
        return res


    def change(self, x, y, board):
        DIRS = [(0,1),(0,-1),(-1,0),(1,0)]
        if board[x][y] == 'O':
            board[x][y] = 'X'
            for dx, dy in DIRS:
                newx = x + dx
                newy = y + dy
                self.change(newx, newy, board)
