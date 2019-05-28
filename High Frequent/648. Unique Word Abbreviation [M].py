class ValidWordAbbr:
    """
    @param: dictionary: a list of words
    """
    def __init__(self, dictionary):
        # do intialization if necessary
        self.h = dict()
        for word in dictionary:
            abbr = ValidWordAbbr.convert(word)
            if abbr not in self.h:
                self.h[abbr] = set()
            self.h[abbr].add(word)

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here
        abbr = ValidWordAbbr.convert(word)
        if abbr in self.h:
            s = self.h[abbr]
            if word not in s or len(s) > 1:
                return False
        return True


    @staticmethod
    def convert(word):
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]
# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)
