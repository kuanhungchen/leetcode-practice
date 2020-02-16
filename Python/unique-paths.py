class Solution:
    def uniquePaths(self, m, n):
        def fact(s):
            return 1 if s == 1 else s * fact(s - 1)

        if m == 0 or n == 0: return 0
        if m == 1 or n == 1: return 1
        
        right, down = m - 1, n - 1
        ans = fact(right + down) // (fact(right) * fact(down))
        return ans

