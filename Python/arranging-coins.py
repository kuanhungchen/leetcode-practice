class Solution:
    def arrangeCoins(self, n):
        if n == 0:
            return n
        left, right = 0, n
        while left + 1 < right:
            mid = (left + right) // 2
            if mid * (mid - 1) // 2 <= n < mid * (mid + 1) // 2:
                return mid - 1
            elif n == mid * (mid + 1) // 2:
                return mid
            elif mid * (mid - 1) // 2 > n:
                right = mid
            else:
                left = mid
        return right if n >= right * (right + 1) // 2 else left
