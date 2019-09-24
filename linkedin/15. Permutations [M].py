## my most issue with this is to keep track of visited list without creating a
## set/list for each method call. visited solves this with a special hash.
## weirdly, this has a slower speed. sets can also help instead of visited.
## set.remove and set.add are both fast.
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        res = []
        self.dfs(nums, [], res, [False for _ in range(len(nums))])
        return res

    def dfs(self, nums, template, res, visited):
        if len(template) == len(nums):
            res.append(template[:])
            return

        for i in range(len(nums)):
            num = nums[i]
            if not visited[i]:
                template.append(num)
                visited[i] = True
                self.dfs(nums, template, res, visited)
                visited[i] = False
                template.pop()

class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        res = []
        self.dfs(nums, [], res, set())
        return res

    def dfs(self, nums, template, res, visited):
        if len(template) == len(nums):
            res.append(template[:])
            return

        for num in nums:
            if num not in visited:
                template.append(num)
                visited.add(num)
                self.dfs(nums, template, res, visited)
                visited.remove(num)
                template.pop()

## my first try.
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        res = []
        self.dfs(nums, [], res)
        return res

    def dfs(self, nums, template, res):
        if len(template) == len(nums):
            res.append(template[:])
            return

        for num in nums:
            if num not in template:
                template.append(num)
                self.dfs(nums, template, res)
                template.pop()
