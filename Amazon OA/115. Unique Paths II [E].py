class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        col1 = [0 for _ in range(r)]
        col2 = list(col1)
        col1[0] = 1
        for i in range(c):
            for j in range(r):
                if obstacleGrid[j][i] == 1:
                    col2[j] = 0
                else:
                    up = col2[j - 1] if j > 0 else 0
                    col2[j] = up + col1[j]
            col1, col2 = col2, [0 for _ in range(r)]
        return col1[-1]
