class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        # write your code here
        map = [0] * 256
        for i in range(len(s)):
            map[ord(s[i])] += 1
        for i in range(len(t)):
            map[ord(t[i])] -= 1
        for i in range(len(map)):
            if map[i] != 0:
                return False
        return True
        
