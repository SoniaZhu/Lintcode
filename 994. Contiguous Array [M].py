class Solution:
    """
    @param nums: a binary array
    @return: the maximum length of a contiguous subarray
    """
    def findMaxLength(self, nums):
        # Write your code here
        ans = 0
        hash = {}
        sum = 0
        for i in range(len(nums)):
            sum += -1 if nums[i] == 0 else 1
            if sum == 0:
                ans = i + 1
            elif sum in hash:
                ans = max(i - hash[sum], ans)
            else:
                hash[sum] = i
        return ans
