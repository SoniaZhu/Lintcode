# pay attention to 0
class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        if not nums:
            return 0
        res = prevMax = prevMin = nums[0]
        for num in nums[1:]:
            if num > 0:
                localMax = max(num, prevMax * num)
                localMin = min(num, prevMin * num)
            else:
                localMax = max(num, prevMin * num)
                localMin = min(num, prevMax * num)
            res = max(res, localMax)
            prevMax, prevMin = localMax, localMin
        return res
