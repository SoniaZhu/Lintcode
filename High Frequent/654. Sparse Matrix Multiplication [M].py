class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        l = len(B)
        res = [[0] * len(B[0]) for i in range(len(A))]
        for r in range(len(A)):
            for c in range(len(B[0])):
                for i in range(l):
                    res[r][c] += A[r][i] * B[i][c]

        return res
