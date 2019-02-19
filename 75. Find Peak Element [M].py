class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        left = 0
        right = len(A) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid - 1] > A[mid]:
                right = mid
            else:
                left = mid
        if A[left] < A[right]:
            return right
        return left

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # # write your code here
        # for i in range(1, len(A) - 1):
        #     if A[i] > A[i + 1]:
        #         return i
        # return -1
        left = 0      # left = 1
        right = len(A) - 1       # right = len(A) - 2
        while left + 1 < right:
            mid = (left + right) // 2
            if A[mid - 1] > A[mid]:
                right = mid
            elif A[mid + 1] > A[mid]:
                left = mid
            else:
                return mid
        return left
