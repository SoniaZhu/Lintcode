class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def isNumber(self, s):
        # write your code here
        s = s.strip() + " "
        length = len(s) - 1
        i = 0
        if self.isPlusMinus(s[i]):
            i += 1

        nPoint, nDigit = 0, 0
        while s[i].isdigit() or s[i] == ".":
            if s[i].isdigit():
                nDigit += 1
            elif s[i] == ".":
                nPoint += 1
            i += 1
        if nPoint > 1 or nDigit < 1:
            return False

        if s[i] == "e":
            i += 1
            if self.isPlusMinus(s[i]):
                i += 1
            if i == length:
                return False
            while s[i].isdigit():
                i += 1
        return i == length

    def isPlusMinus(self, c):
        if c == "+" or c == "-":
            return True
        else:
            return False
