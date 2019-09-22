class Solution:
    def isPerfectSquare(self, num):
        left = 1
        right = num // 2
        while left + 1 < right:
            mid = (left + right) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                left = mid
            else:
                right = mid
        return True if left ** 2 == num or right ** 2 == num else False
