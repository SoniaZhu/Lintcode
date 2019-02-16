class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalpha() and not s[l].isdigit():
                l += 1
            elif not s[r].isalpha() and not s[r].isdigit():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
