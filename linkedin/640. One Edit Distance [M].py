## pay attention to [ab(c)] [ab]
class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        distance = 0
        si = ti = 0
        while si < len(s) and ti < len(t):
            if s[si] != t[ti]:
                if distance == 1:
                    return False
                else:
                    distance += 1
                    if len(s) < len(t):
                        si -= 1
                    elif len(s) > len(t):
                        ti -= 1
            si += 1
            ti += 1
        if si == len(s) and ti == len(t) and distance == 1:
            return True
        elif ti == len(t) - 1 or si == len(s) - 1:
            return True
        else:
            return False
