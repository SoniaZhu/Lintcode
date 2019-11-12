class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        map = dict()
        maxLen = float('-inf')
        for r in range(len(s)):
            if s[r] in map:
                prevIndex = map[s[r]]
                for i in range(l , prevIndex + 1):
                    del map[s[i]]
                l = prevIndex + 1
            map[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
        return maxLen

# Python 3.x
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        unique_chars = set([])
        j = 0
        n = len(s)
        longest = 0
        for i in range(n):
            while j < n and s[j] not in unique_chars:
                unique_chars.add(s[j])
                j += 1
            longest = max(longest, j - i)
            unique_chars.remove(s[i])

        return longest
