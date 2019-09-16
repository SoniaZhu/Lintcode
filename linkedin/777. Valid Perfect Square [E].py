class Solution:
    """
    @param num: a positive integer
    @return: if num is a perfect square else False
    """
    def isPerfectSquare(self, num):
        # write your code here
        if num == 1:
            return True
        left = 1
        right = num // 2

        while left <= right:
            mid = left + (right - left) // 2
            product = mid * mid
            if product == num:
                return True
            if product < num:
                left = mid + 1
            elif product > num:
                right = mid - 1

        return False
