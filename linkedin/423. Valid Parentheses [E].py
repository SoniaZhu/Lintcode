# fast do not perfect
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif c == ")" or c == "]" or c == "}":
                if not stack or stack[-1] != self.helper(c):
                    return False
                stack.pop()
        return not stack

    def helper(self, c):
        if c == ")":
            return "("
        if c == "]":
            return "["
        if c == "}":
            return "{"


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
