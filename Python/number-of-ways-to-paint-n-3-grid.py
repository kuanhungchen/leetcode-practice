class Solution:
    def numOfWays(self, n):
        if n == 1: return 12
        mod = 10 ** 9 + 7
        a, b = 2, 9
        for i in range(n - 2):
            a = 5 * b - 2 * a
            a, b = b, a
        return 6 * b % mod
