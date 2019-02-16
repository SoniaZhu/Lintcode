class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        l = 0
        r = len(A) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if A[mid] <= A[r]:
                if target >= A[mid] and target <= A[r]:
                    l = mid
                else:
                    r = mid - 1   # can be r = mid
            else:
                if target < A[mid] and target >= A[l]:
                    r = mid - 1    # can be r = mid
                else:
                    l = mid
        if A[l] == target:
            return l
        elif A[r] == target:
            return r
        else:
            return -1
