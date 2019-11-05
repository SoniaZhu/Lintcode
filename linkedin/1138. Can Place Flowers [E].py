class Solution:

    def canPlaceFlowers(self, flowerbed, n):

        if n == 0: return True
        if not flowerbed: return False

        placed = 0
        left, mid, right = 0, 0, flowerbed[0]

        for i in range(len(flowerbed)-1):

            left, mid, right = mid, right, flowerbed[i+1]
            if not (left or mid or right):
                placed += 1
                mid = 1

            if placed == n:
                return True

        if not (mid or right):
            placed += 1

        return placed >= n
        
# WRONG BELOW
# class Solution:
#     """
#     @param flowerbed: an array
#     @param n: an Integer
#     @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
#     """
#     def canPlaceFlowers(self, flowerbed, n):
#         # Write your code
#         count = 0
#         total = 0
#         lst = flowerbed + [1]
#         for i in lst:
#             if i == 0:
#                 count += 1
#             elif i == 1 and count != 0:
#                 total += (count - 1) // 2
#                 count = 0
#                 if total >= n:
#                     return True
#
#         return False
#
#
# class Solution:
#     """
#     @param flowerbed: an array
#     @param n: an Integer
#     @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
#     """
#     def canPlaceFlowers(self, flowerbed, n):
#         # Write your code
#         count = 0
#         total = 0
#         for i in range(len(flowerbed) + 1):
#             if i == len(flowerbed) or flowerbed[i] == 1:
#                 if count != 0:
#                     total += (count - 1) // 2
#                     count = 0
#                     if total >= n:
#                         return True
#             elif flowerbed[i] == 0:
#                 count += 1
#
#         return False
