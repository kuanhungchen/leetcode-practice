class Solution:
    def sumZero(self, n):
        if n % 2 == 0:
            return [-x for x in range(1, n // 2 + 1)] + [x for x in range(1, n // 2 + 1)]
        else:
            return [-x for x in range(1, n // 2 + 1)] + [0] + [x for x in range(1, n // 2 + 1)]
