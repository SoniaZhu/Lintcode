## don't know how to do
## https://www.youtube.com/watch?v=yEQq3t3T_J0
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0 :
            x = 1 / x
            n = -n

        ans = 1
        tmp = x

        while n != 0:
            if n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            n //= 2
        return ans

class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        if n < 0 :
            x = 1 / x
            n = -n

        if n == 0:
            return 1
        y = self.myPow(x, n // 2)
        if n % 2 == 0:
            return y * y
        else:
            return y * y * x
