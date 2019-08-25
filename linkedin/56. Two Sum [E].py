class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hash = dict()
        for i in range(len(numbers)):
            if target - numbers[i] in hash:
                return [hash[target - numbers[i]], i]
            else:
                hash[numbers[i]] = i
        return [-1, -1]

    ## mine. bad. 
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        hash = dict()
        for i in range(len(numbers)):
            hash[numbers[i]] = i
        for i in range(len(numbers)):
            if (target - numbers[i]) in hash:
                anotherIndex = hash[target - numbers[i]]
                return [min(anotherIndex, i), max(anotherIndex, i)]
        return []
