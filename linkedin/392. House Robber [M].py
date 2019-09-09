## mine
class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        globalMax = 0
        localMax = 0
        for num in A:
            localMax, globalMax = globalMax, max(globalMax, num + localMax)
        return globalMax

## java. O(n) memory instead O(1) but is DP
public class Solution {
    /**
     * @param A: An array of non-negative integers.
     * return: The maximum amount of money you can rob tonight
     */
    public long houseRobber(int[] A) {
        int n = A.length;
        if (n == 0)
            return 0;
        long []res = new long[n+1];

        res[0] = 0;
        res[1] = A[0];
        for (int i = 2; i <= n; i++) {
            res[i] = Math.max(res[i-1], res[i-2] + A[i-1]);
        }
        return res[n];
    }
}
