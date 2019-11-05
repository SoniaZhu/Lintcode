class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid

        resLeft = -1
        if nums[l] == target:
            resLeft = l
        elif nums[r] == target:
            resRight = r
        else:
            return [-1, -1]

        l = resLeft
        r = len(nums) - 1
        while l + 1 < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] == target:
                l = mid
            else:
                r = mid - 1
        if nums[r] == target:
            return [resLeft, r]

        return [resLeft, l]
