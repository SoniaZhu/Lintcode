class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        # write your code here
        if len(dict) == 0:
            return s == ''
        n = len(s)
        mem = [False] * (n + 1)
        mem[0] = True
        maxLength = max([len(x) for x in dict])
        for i in range(1, n + 1):   # py2 xrange
            for j in range(1, min(maxLength, i) + 1):
                if s[i - j: i] in dict and mem[i - j]:
                    mem[i] = True
                    break
        return mem[-1]


# [ i            ]
# [mem][j in dict]
