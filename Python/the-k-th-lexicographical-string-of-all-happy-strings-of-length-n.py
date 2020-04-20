class Solution:
    def getHappyString(self, n, k):
        self.k = k

        def solve(s):
            if len(s) == n:
                self.k -= 1
                return s if not self.k else 0
            if s[-1] == 'a':
                res = solve(s + 'b')
                if res: return res
                res = solve(s + 'c')
                if res: return res
            elif s[-1] == 'b':
                res = solve(s + 'a')
                if res: return res
                res = solve(s + 'c')
                if res: return res
            else:
                res = solve(s + 'a')
                if res: return res
                res = solve(s + 'b')
                if res: return res

        return solve('a') or solve('b') or solve('c') or ""
