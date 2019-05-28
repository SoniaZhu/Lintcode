class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):
        # Write your code here
        digits = []
        letters = []
        for i in range(len(logs)):
            if logs[i].strip()[-1].isdigit():
                digits.append(logs[i])
            else:
                letters.append(logs[i])

        return sorted(letters, key = Solution.myKey) + digits

    @staticmethod
    def myKey(log):
        idx = log.index(' ')
        return (log[idx + 1:], log[:idx])
        
