# mine. not the best. three sols READ! https://www.jiuzhang.com/solution/maximum-subarray/
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        small = [0]
        smallSum = 0
        for i in range(len(nums) - 1):
            smallSum += nums[i]
            small.append(smallSum if smallSum < small[-1] else small[-1])
        largeSum = 0
        res = float('-inf')
        for i in range(len(nums)):
            largeSum += nums[i]
            res = max(res, largeSum - small[i])
        return res
