class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == '0':
                    return False
                val = 0
                while j < len(abbr) and abbr[j].isdigit():
                    val = val * 10 + int(abbr[j])   # ord
                    j += 1
                i += val
            else:
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)
