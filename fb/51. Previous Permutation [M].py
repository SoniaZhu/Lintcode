class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                break
        else:
            nums.reverse()
            return nums

        for j in range(len(nums) - 1, i, -1):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                break

        for j in range((len(nums) - 1 - i) // 2):
            nums[i + 1 + j], nums[len(nums) - 1 - j] = nums[len(nums) - 1 - j], nums[i + 1 + j]
        return nums
