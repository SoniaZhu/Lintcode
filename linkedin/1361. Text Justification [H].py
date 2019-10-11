## very easy to make errors
class Solution:
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """
    def fullJustify(self, words, maxWidth):
        res = []
        line = []
        lineLen = 0
        for word in words:
            if len(word) + len(line) + lineLen > maxWidth:
                res.append(self.format(line, maxWidth))
                line = []
                lineLen = 0
            line.append(word)
            lineLen += len(word)

        res.append(self.formatLastLine(line, maxWidth))
        return res

    def format(self, line, maxWidth):
        if len(line) == 1:
            return line[0] + ' ' * (maxWidth - len(line[0]))
        lenSum = sum([len(w) for w in line])
        space = (maxWidth - lenSum) // (len(line) - 1)
        reminder = (maxWidth - lenSum) % (len(line) - 1)
        res = line[0]
        for i in range(1, len(line)):
            res += ' ' * space + (' ' if i - 1 < reminder else '') + line[i]
        return res

    def formatLastLine(self, line, maxWidth):
        res = ' '.join(line)
        return res + ' ' * (maxWidth - len(res))

## My solution.
class Solution:
    """
    @param words: an array of string
    @param maxWidth: a integer
    @return: format the text such that each line has exactly maxWidth characters and is fully
    """
    def fullJustify(self, words, maxWidth):
        # write your code here
        res = []
        p = Parser(words, maxWidth)
        while p.hasNext():
            p.readLine(res)
        return res

class Parser:
    def __init__(self, words, maxWidth):
        self.words = words
        self.startIndex = 0
        self.maxWidth = maxWidth
        self.endIndex = -1
        self.count = -1

    def readLine(self, res):
        if not self.hasNext():
            return

        if not self.isLastLine() and self.endIndex != self.startIndex:
            space = (self.maxWidth - self.count) // (self.endIndex - self.startIndex)
            reminder = (self.maxWidth - self.count) % (self.endIndex - self.startIndex)
        else:
            space = 0
            reminder = 0

        one = ''
        for i in range(self.startIndex, self.endIndex + 1):
            one += self.words[i]
            if i != self.endIndex:
                one += ' ' * (space + (1 if i - self.startIndex < reminder else 0)) + ' '
        one += ' ' * (self.maxWidth - len(one))
        res.append(one)
        self.startIndex = self.endIndex + 1
        self.endIndex = -1
        self.count = -1

    def isLastLine(self):
        if not self.hasNext():
            return False
        if self.endIndex == -1:
            totalCount = -1
            for i in range(self.startIndex, len(self.words)):
                totalCount += len(self.words[i]) + 1
                if totalCount > self.maxWidth:
                    break

            if totalCount > self.maxWidth:
                self.count = totalCount - len(self.words[i]) - 1
                self.endIndex = i - 1
            else:
                self.endIndex = i
                self.count = totalCount
        return self.endIndex == len(self.words) - 1

    def hasNext(self):
        return self.startIndex < len(self.words)
