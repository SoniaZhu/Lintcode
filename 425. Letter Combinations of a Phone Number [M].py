# 第二次做
class Solution:
    KEYBOARD = {
        '1': [''],
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        self.helper(digits, 0, [], res)
        return res

    def helper(self, digits, index, template, res):
        if index >= len(digits):
            res.append(''.join(template))
            return
        for letter in self.KEYBOARD[digits[index]]:
            template.append(letter)
            self.helper(digits, index + 1, template, res)
            template.pop()

class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    # chr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
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

# class Solution:
#     """
#     @param digits: A digital string
#     @return: all posible letter combinations
#     """
#     def letterCombinations(self, digits):
#         chr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#         res = []
#         for i in range(0, len(digits)):
#             num = int(digits[i])
#             tmp = []
#             for j in range(0, len(chr[num])):
#                 if len(res):
#                     for k in range(0, len(res)):
#                         tmp.append(res[k] + chr[num][j])
#                 else:
#                     tmp.append(str(chr[num][j]))
#             res = copy.copy(tmp)
#         return res
