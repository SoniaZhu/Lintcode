class Solution:
    """
    @param temperatures: a list of daily temperatures
    @return: a list of how many days you would have to wait until a warmer temperature
    """
    def dailyTemperatures(self, temperatures):
        # Write your code here
        if not temperatures:
            return []
        queue = [(0)]
        res = [0 for _ in temperatures]
        for i in range(1, len(temperatures)):
            while queue and temperatures[i] > temperatures[queue[-1]]:
                index = queue.pop()
                res[index] = i - index
            queue.append(i)
        return res
