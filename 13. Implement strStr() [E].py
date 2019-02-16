class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        n = len(target)
        for i in range(len(source) - n + 1):
            if source[i:i + n] == target:
                return i
        return -1
