class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return "0"
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10+int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                sign = s[i]
                num = 0
        return sum(stack)

# def isValidIPv4Part(self, str):
#         if not str:
#             return False
#         for c in str:
#             if not c.isdigit():
#                 return False
#         if str[0] == '0' and str != '0':
#             return False
#         return int(str) <= 255
