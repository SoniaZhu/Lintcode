# class Solution:
#     """
#     @param a: a number
#     @param b: a number
#     @return: the result
#     """
#     def addBinary(self, a, b):
#         # write your code here
#         if len(a) > len(b):
#             longer = a[::-1]
#             shorter = b[::-1] + ''.join(['0'] * (len(a) - len(b)))
#         else:
#             longer = b[::-1]
#             shorter = a[::-1] + ''.join(['0'] * (len(b) - len(a)))
#         carry = 0
#         res = ''
#         for i in range(len(longer)):
#             sum = int(longer[i]) + int(shorter[i]) + carry
#             res += str(sum % 2)
#             carry = int(sum / 2)
#         if carry == 1:
#             res += '1'
#         return ''.join(res[::-1])

class Solution:
    """
    @param a: a number
    @param b: a number
    @return: the result
    """
    def addBinary(self, a, b):
        # write your code here
        indexa = len(a) - 1
        indexb = len(b) - 1
        carry = 0
        res = ""
        while indexa >= 0 or indexb >= 0:
            x = int(a[indexa]) if indexa >= 0 else 0
            y = int(b[indexb]) if indexb >= 0 else 0
            res = str((x + y + carry) % 2) + res
            carry = int((x + y + carry) / 2)
            indexa -= 1
            indexb -= 1
        if carry == 1:
            res = '1' + res
        return res
