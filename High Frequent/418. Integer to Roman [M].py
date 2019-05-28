class Solution:
    NUMS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    LETTERS = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    """
    @param n: The integer
    @return: Roman representation
    """
    def intToRoman(self, n):
        # write your code here
        index = 0
        res = ''
        while n > 0:
            if n >= self.NUMS[index]:
                n -= self.NUMS[index]
                res += self.LETTERS[index]
            else:
                index += 1
        return res

#############################
    def intToRoman(self, n):
        # write your code here
        res = ''
        for d, r in zip(NUMS, LETTERS):
            result += r * (n // d)
            n %= d
        return result
