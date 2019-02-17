## what I will do it myself. struggling....
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s or s == '0':
            return 0
        mem = [1] * (len(s) + 1)
        for i in range(2, len(s) + 1):
            if s[i - 1] == '0':
                if s[i - 2] == '1' or s[i - 2] == '2':
                    mem[i] = mem[i - 2]
                else:
                    mem[i] = 0
            elif 10 < int(s[i - 2: i]) <= 26:
                mem[i] = mem[i - 1] + mem[i - 2]
            else:
                mem[i] = mem[i - 1]
        return mem[-1]

## if x0, 1) 10 or 20 -> -2  2) 0
## 10 - 26:  -1 + -2
## else - 1  (0x  88)

# Right Answer py2:
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        if s == "" or s == "0":
            return 0

        dp = [1,1]
        for i in range(2, len(s) + 1):
            if s[i - 1] == '0':
                if s[i - 2 : i] == "20" or int(s[i - 2 : i]) == 10:
                    dp.append(dp[i - 2])
                else:
                    return 0
            elif 10 <= int(s[i - 2 : i]) <= 26:
                dp.append(dp[i - 2] + dp[i - 1])
            else:
                dp.append(dp[i - 1])
        return dp[-1]
