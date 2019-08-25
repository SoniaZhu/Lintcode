class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, mem):
        if s in mem:
            return mem[s]
        res = []
        if s in wordDict:
            res.append(s)
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue
            partRes = self.dfs(s[i:], wordDict, mem)
            for partS in partRes:
                res.append(prefix + " " + partS)
        mem[s] = res
        return res
