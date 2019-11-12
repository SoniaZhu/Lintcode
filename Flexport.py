import random
import collections
def generateStr(corpus, n):
    if not corpus:
        return ""
    mapToIndex = collections.defaultdict(list)
    corpusList = corpus.split()
    for i in range(len(corpusList)):
        mapToIndex[corpusList[i]].append(i)
    res = []
    word = random.choice(corpusList)
    res.append(word)
    for _ in range(n - 1):
        nextIndex = random.choice(mapToIndex[word]) + 1
        if nextIndex >= len(corpusList):
            nextIndex = 0
        word = corpusList[nextIndex]
        res.append(word)
    return res

print (generateStr("let us go to the supermarket to get the to go bundle", 5))

##
import collections
class Money:
    def __init__(self, blk, blue, green, white):
        self.blk = blk
        self.blue = blue
        self.green = green
        self.white = white

    def isLargerEq(self, other):
        return self.blk >= other.blk and self.blue >= other.blue and self.green >= other.green and self.white >= other.white

    def times(self, multiplier):
        return Money(multiplier * self.blk, multiplier * self.blue, multiplier * self.green, multiplier * self.white)

    def subtract(self, other):
        return Money(
        self.blk - other.blk,
        self.blue - other.blue,
        self.green - other.green,
        self.white - other.white)

    def __str__(self):
      return f"{self.blk}, {self.blue}, {self.green}, {self.white}"

class Card:
    DISCOUNT = 0.9
    def __init__(self, moneyValue, colorType):
        self.moneyValue = moneyValue
        self.colorType = colorType
    def __str__(self):
      return f"{self.colorType}"

class Person:
    def __init__(self, ownMoney, ownCards=[]):
        self.ownMoney = ownMoney
        self.colorToCards = collections.defaultdict(list)
        for card in ownCards:
            self.colorToCards[card.colorType].append(card)

    def canPurchase(self, card):
        return self.ownMoney.isLargerEq(self.getDiscountedValue(card))

    def getDiscountedValue(self, card):
        cardValue = card.moneyValue
        if card.colorType in self.colorToCards:
            cardValue = cardValue.times(Card.DISCOUNT)
        return cardValue

    def purchase(self, card):
        if self.canPurchase(card):
            self.ownMoney = self.ownMoney.subtract(self.getDiscountedValue(card))
            self.colorToCards[card.colorType].append(card)
            return True
        else:
            return False

m = Money(20,20,20,10)
c = Card(Money(10,10,10,5), "red")
p = Person(m)
p.purchase(c)
print (p.ownMoney, *p.colorToCards["red"])
p.purchase(c)
print (p.ownMoney, *p.colorToCards["red"])



#
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

# [   ]
#   [   ]
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals = sorted(intervals)
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        return res

#
    def isValidIPv4(self, str):
        PERIOD = '.'
        parts = str.split(PERIOD)
        if len(parts) != 4:
            return False
        for part in parts:
            if not self.isValidIPv4Part(part):
                return False
        return True

    def isValidIPv4Part(self, str):
        if not str:
            return False
        for c in str:
            if not c.isdigit():
                return False
        if str[0] == '0' and str != '0':
            return False
        return int(str) <= 255
#

class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return "0"
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10+int(s[i])
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    stack.append(-num)
                elif sign == "+":
                    stack.append(num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                sign = s[i]
                num = 0
        return sum(stack)


#
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        if not s or s == '0':
            return 0
        mem = [1] * (len(s) + 1)
        for i in range(2, len(s) + 1):
            sum = 0
            if 1 <= int(s[i - 1]) <= 9:
                sum += mem[i - 1]
            if 10 <= int(s[i - 2: i]) <= 26:
                sum += mem[i - 2]
            mem[i] = sum
        return mem[-1]
