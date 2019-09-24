## wait, no dp nor mem??? mine is so fast? 99.20%
## think about dup res -> previousNum, set
## maybe better to sort, and if num > target, eliminate all nums following num
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = set(candidates)
        res = []
        self.combinationSumHelper(candidates, target, [], res, 0)
        return res

    def combinationSumHelper(self, candidates, target, template, res, previousNum):
        if target == 0:
            res.append(template[:])
        elif target > 0:
            for number in candidates:
                if number < previousNum:
                    continue
                template.append(number)
                self.combinationSumHelper(candidates, target - number, template, res, number)
                template.pop()


class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = sorted(set(candidates))
        res = []
        self.combinationSumHelper(candidates, target, [], res, 0)
        return res

    def combinationSumHelper(self, candidates, target, template, res, index):
        if target == 0:
            res.append(template[:])
        elif target > 0:
            for i in range(index, len(candidates)):
                number = candidates[i]
                if number > target:
                    return
                template.append(number)
                self.combinationSumHelper(candidates, target - number, template, res, i)
                template.pop()


                
## beat 11% slow. 2^h
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates = sorted(set(candidates))
        res = []
        self.combinationSumHelper(candidates, target, [], res, 0)
        return res

    def combinationSumHelper(self, candidates, target, template, res, index):
        if index == len(candidates) :
            if target == 0:
                res.append(template[:])
            return
        if target < 0:
            return
        self.combinationSumHelper(candidates, target, template, res, index + 1)

        template.append(candidates[index])
        self.combinationSumHelper(candidates, target - candidates[index], template, res, index)
        template.pop()
