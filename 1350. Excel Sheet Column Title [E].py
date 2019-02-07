class Solution:
    """
    @param n: a integer
    @return: return a string
    """
    def convertToTitle(self, n):
        # write your code here
        res = ''
        while n > 0:
            n -= 1
            res += chr(n % 26 + ord('A'))
            n /= 26
        return res[::-1]
