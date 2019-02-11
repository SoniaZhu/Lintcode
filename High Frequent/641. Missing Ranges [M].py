class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
    #     ans = []
    #     if len(nums) == 0:
    #         self.addRange(ans, lower, upper)
    #         return ans
    #     self.addRange(ans, lower, nums[0] - 1)
    #     for i in range(1, len(nums)):
    #         self.addRange(ans, nums[i - 1] + 1, nums[i] - 1)
    #     self.addRange(ans, nums[-1] + 1, upper)
    #     return ans

    # def addRange(self, ans, s, e):
    #     if s > e:
    #         return
    #     if s == e:
    #         ans.append(str(s))
    #     else:
    #         ans.append(str(s) + "->" + str(e))

    # customized version

        ans = []
        nums = [lower + -1] + nums + [upper + 1]
        for i in range(1, len(nums)):
            l = nums[i - 1]
            h = nums[i]
            if h - l == 2:
                ans.append(str(l + 1))
            elif h - l > 2:
                ans.append(str(l + 1) + "->" + str(h - 1))
        return ans
