class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    KEYBOARD = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'}

    def letterCombinations(self, digits):
        # write your code here
        if not digits:
            return []
        res = []
        self.dfs(digits, 0, '', res)
        return res

    def dfs(self, digits, index, template, res):
        if index == len(digits):
            res.append(template)
            return
        for option in self.KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, template + option, res)
