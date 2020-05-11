class Solution:
    def distributeCandies(self, candies):
        return min(len(set(candies)), len(candies) // 2)
