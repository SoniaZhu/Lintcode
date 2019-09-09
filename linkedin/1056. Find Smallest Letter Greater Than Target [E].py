class Solution:
    """
    @param letters: a list of sorted characters
    @param target: a target letter
    @return: the smallest element in the list that is larger than the given target
    """
    def nextGreatestLetter(self, letters, target):
        # Write your code here
        left = 0
        right = len(letters) - 1
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid
        if left == right:
            return letters[left]
        else:
            return letters[0]


class Solution:
    """
    @param letters: a list of sorted characters
    @param target: a target letter
    @return: the smallest element in the list that is larger than the given target
    """
    def nextGreatestLetter(self, letters, target):
        # Write your code here
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
