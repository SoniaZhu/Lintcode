class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        # write your code here
        ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        if s == '':
            return 0

        sum = ROMAN[s[-1]]
        for i in range(len(s) - 2, -1, -1):
            if ROMAN[s[i]] < ROMAN[s[i + 1]]:
                sum -= ROMAN[s[i]]
            else:
                sum += ROMAN[s[i]]
        return sum
