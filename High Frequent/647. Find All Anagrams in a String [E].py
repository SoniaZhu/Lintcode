class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        # write your code here
        res = []
        maps = [0]*26
        mapp = [0]*26

        for i in range(len(p)):
            maps[ord(p[i]) - ord('a')] += 1

        for i in range(0, len(s)):
            if i >= len(p):
                mapp[ord(s[i - len(p)]) - ord('a')] -= 1
            mapp[ord(s[i]) - ord('a')] += 1
            if mapp == maps:
                res.append(i - len(p) + 1)
        return res
