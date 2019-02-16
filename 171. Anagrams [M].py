class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        # write your code here
        res = []
        dict = {}
        for str in strs:
            sortedStr = "".join(sorted(str))
            dict[sortedStr] = [str] if sortedStr not in dict else dict[sortedStr] + [str]
        for key in dict:
            if len(dict[key]) >= 2:
                res += dict[key]
        return res
