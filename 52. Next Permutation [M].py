class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        else:
            nums.reverse()
            return nums

        for j in range(len(nums) - 1, i, -1):
            if nums[j] > nums[i]:
                break
        nums[i], nums[j] = nums[j], nums[i]

        for j in range((len(nums) - i - 1) // 2):
            nums[i + 1 + j], nums[len(nums) - 1 - j] = nums[len(nums) - 1 - j], nums[i + 1 + j]
        return nums

# my own complex version
class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        index = -1
        for i in range (len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        nextIndex = index + 1
        for i in range(index + 1, len(nums)):
            if nums[i] > nums[index] and nums[i] <= nums[nextIndex]:
                nextIndex = i

        if index != -1:
            nums[index], nums[nextIndex] = nums[nextIndex], nums[index]

        # index + 1 -> len(nums) - 1
        left = index + 1
        right = len(nums) - 1
        while (left < right):
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums
