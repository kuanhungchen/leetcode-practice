class Solution:
    def maxPower(self, s):
        mx, res = 0, 1
        now = s[0]
        for c in s[1:]:
            if now == c:
                res += 1
            else:
                mx = max(mx, res)
                res = 1
                now = c
        mx = max(mx, res)
        return mx
