class Solution:
    def tribonacci(self, n):
        t = [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
        if n < 10:
            return t[n]
        for _ in range(n-9):
            t.append(t[-1] + t[-2] + t[-3])
        return t[-1]
