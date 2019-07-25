class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    def canPlaceFlowers(self, flowerbed, n):
        # Write your code
        count = 0
        total = 0
        lst = flowerbed + [1]
        for i in lst:
            if i == 0:
                count += 1
            elif i == 1 and count != 0:
                total += (count - 1) // 2
                count = 0
                if total >= n:
                    return True

        return False


class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    def canPlaceFlowers(self, flowerbed, n):
        # Write your code
        count = 0
        total = 0
        for i in range(len(flowerbed) + 1):
            if i == len(flowerbed) or flowerbed[i] == 1:
                if count != 0:
                    total += (count - 1) // 2
                    count = 0
                    if total >= n:
                        return True
            elif flowerbed[i] == 0:
                count += 1

        return False
