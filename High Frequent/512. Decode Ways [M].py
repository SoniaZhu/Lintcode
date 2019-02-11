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
