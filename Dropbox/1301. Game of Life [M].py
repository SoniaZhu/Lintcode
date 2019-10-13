class Solution:
    """
    @param board: the given board
    @return: nothing
    """
    def gameOfLife(self, board):
        # Write your code here
        r, c = len(board), len(board[0]);
        for i in range(r):
            for j in range(c):
                lives = Solution.getNearbyLives(i, j, board)
                # ## 1 -> 1 1
                # if board[i][j] == 1 and (lives == 2 or lives == 3):
                #     board[i][j] = 3
                # ## 0 -> 1 0
                # elif board[i][j] == 0 and lives == 3:
                #     board[i][j] = 2

                if lives == 3 or (board[i][j] == 1 and lives == 2):
                    board[i][j] |= 2
        for i in range(r):
            for j in range(c):
                board[i][j] >>= 1

    @staticmethod
    def getNearbyLives(x, y, board):
        r, c = len(board), len(board[0]);
        count = 0
        for i in range(max(x - 1, 0), min(x + 1, r - 1) + 1):
            for j in range(max(y - 1, 0), min(y + 1, c - 1) + 1):
                count += board[i][j] & 1
        return count - (board[x][y] & 1)


class Solution:
    """
    @param board: the given board
    @return: nothing
    """
    def gameOfLife(self, board):
        # Write your code here
        r, c = len(board), len(board[0]);
        temp = [[0 for i in range(c)] for j in range(r)]

        for i in range(r):
            for j in range(c):
                lives = Solution.getNearbyLives(i, j, board)
                if board[i][j] == 1 and (lives < 2 or lives > 3):
                    temp[i][j] = 0
                elif board[i][j] == 0 and lives == 3:
                    temp[i][j] = 1
                else:
                    temp[i][j] = board[i][j]

        board[::] = temp[::]

    @staticmethod
    def getNearbyLives(x, y, board):
        r, c = len(board), len(board[0]);
        count = 0
        for i in range(max(x - 1, 0), min(x + 1, r - 1) + 1):
            for j in range(max(y - 1, 0), min(y + 1, c - 1) + 1):
                count += board[i][j]
        return count - board[x][y]
