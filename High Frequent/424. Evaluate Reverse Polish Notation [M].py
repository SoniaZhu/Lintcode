from collections import deque
class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        # write your code here
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self._calculate(op1, op2, token))
        return stack.pop()

    def _calculate(self, op1, op2, operator):
        if operator == "+":
            return op1 + op2
        elif operator == "-":
            return op1 - op2
        elif operator == "*":
            return op1 * op2
        elif operator == "/":
            return int(op1 / op2)
