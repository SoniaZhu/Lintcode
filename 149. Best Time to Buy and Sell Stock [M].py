class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        if len(prices) == 0:
            return 0

        # float("inf") 
        min = prices[0]
        diff = 0
        for num in prices:
            if num < min:
                min = num
            else:
                diff = max(diff, num - min)
        return diff
