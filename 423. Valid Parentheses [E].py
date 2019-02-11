class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        LEFT = {'(' : ')' ,'{' : '}', '[' : ']'}
        stack = []
        for c in s:
            if c in LEFT:
                stack.append(c)
            elif len(stack) == 0 or c != LEFT[stack.pop()]:
                return False
        return len(stack) == 0

    ## left: append. right: return false if stack is empty or not match.
    ## finally return whether stack is empty
