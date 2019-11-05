class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs:
            return 0
        previous = costs[0]
        current = [0, 0, 0]
        for i in range(1, len(costs)):
            for c in range(3):
                current[c] = costs[i][c] + min(previous[(c + 1) % 3], previous[(c + 2) % 3])
            ## important
            previous, current = current, previous
        return min(previous)




# mine 1 try. mem. very slow. red, blue or green [0, 1, 2]
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        if not costs:
            return 0
        mem = dict()
        return self.minCostHelper(costs, 0, -1, mem)

    def minCostHelper(self, costs, i, exclude, mem):
        if i >= len(costs):
            return 0
        if (exclude, i) in mem:
            return mem[(exclude, i)]
        total = float('inf')
        for color in range(3):
            if color != exclude:
                total = min(total, costs[i][color] + self.minCostHelper(costs, i + 1, color, mem))
        mem[(exclude, i)] = total
        return total

# second try dp. beats 54.80.
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        if not costs:
            return 0
        n = len(costs)
        dp = [[0, 0, 0] for _ in range(n)]
        for i in range(3):
            dp[-1] = costs[-1]
        for h in range(n-2, -1, -1):
            for c in range(3):
                dp[h][c] = costs[h][c] + min(dp[h+1][(c+1)%3], dp[h+1][(c+2)%3])
        return min(dp[0])

# third try.
class Solution:
    """
    @param costs: n x 3 cost matrix
    @return: An integer, the minimum cost to paint all houses
    """
    def minCost(self, costs):
        # write your code here
        if not costs:
            return 0
        next = costs[-1]
        previous = [0, 0, 0]
        for h in range(len(costs)-2, -1, -1):
            for c in range(3):
                previous[c] = costs[h][c] + min(next[(c+1)%3], next[(c+2)%3])
            previous, next = [0, 0, 0], previous
        return min(next)
