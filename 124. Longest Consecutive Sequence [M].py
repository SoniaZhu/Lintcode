class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # write your code here
        hash = set(num)
        ans = 0
        for n in num:
            if n in hash:
                # hash.remove(n)
                left = n - 1
                right = n + 1
                while left in hash:
                    hash.remove(left)
                    left -= 1
                while right in hash:
                    hash.remove(right)
                    right += 1
                ans = max(ans, right - left - 1)
        return ans
