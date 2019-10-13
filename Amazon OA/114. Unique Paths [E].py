class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        col1 = [1 for _ in range(m)]
        for i in range(1, len(col1)):
            col1[i] = 0
        col2 = [1 for _ in range(m)]
        for _ in range(n):
            for i in range(len(col2)):
                up = col2[i - 1] if i > 0 else 0
                col2[i] = col1[i] + up

            col1, col2 = col2, [1 for _ in range(m)]

        return col1[-1]
