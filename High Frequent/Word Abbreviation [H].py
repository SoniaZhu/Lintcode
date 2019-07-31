class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def wordsAbbreviation(self, dict):
        # write your code here
        hash = {}
        res = [-1] * len(dict)
        round = 1
        for index in range(len(dict)):
            res[index] = Solution.convert(dict[index], round)
            hash[res[index]] = hash.get(res[index], 0) + 1

        while True:
            unique = True
            round += 1
            for index in range(len(dict)):
                if hash[res[index]] > 1:
                    unique = False
                    res[index] = Solution.convert(dict[index], round)
                    hash[res[index]] = hash.get(res[index], 0) + 1
            if unique:
                break
        return res

    @staticmethod
    def convert(word, prefixLen):
        if len(word) <= 2 + prefixLen:
            return word
        else:
            return word[:prefixLen] + str(len(word) - prefixLen - 1) + word[-1]







## Am  vs AlogA + Am










class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def wordsAbbreviation(self, dict):
        # write your code here
        hash = {}
        res = [-1] * len(dict)
        for i in range(len(dict)):
            word = dict[i]
            abbr = Solution.convert(word, 1)
            if abbr in hash:
                hash[abbr].append(i)
            else:
                hash[abbr] = [i]
        for abbr, idxs in hash.items():
            if len(idxs) == 1:
                res[idxs[0]] = abbr
                continue
            words = [(dict[i], i) for i in idxs]
            words.sort()
            for i in range(len(words)):
                word, index = words[i]
                preLen = -1
                nextLen = -1
                if i > 0:
                    preLen = Solution.prefixLength(word, words[i - 1][0])
                if i < len(words) - 1:
                    nextLen = Solution.prefixLength(word, words[i + 1][0])
                res[index] = Solution.convert(word, max(preLen, nextLen))
        return res

    @staticmethod
    def convert(word, prefixLen):
        if len(word) <= 2 + prefixLen:
            return word
        else:
            return word[:prefixLen] + str(len(word) - prefixLen - 1) + word[-1]

    @staticmethod
    def prefixLength(w1, w2):
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                break
        return i + 1
