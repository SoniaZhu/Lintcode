class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        left = 0
        right = x
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * mid <= x:
                left = mid
            else:
                right = mid
        if right * right <= x:
            return right
        return left
        
