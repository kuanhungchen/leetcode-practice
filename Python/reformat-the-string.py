class Solution:
    def reformat(self, s):
        a, b = [], []
        for c in s:
            if c.isdigit():
                a.append(c)
            else:
                b.append(c)
        if abs(len(a) - len(b)) > 1: return ""
        ans = ""
        if len(a) == len(b):
            for x, y in zip(a, b):
                ans += x + y
            return ans
        elif len(a) > len(b):
            for x, y in zip(a, b):
                ans += x + y
            ans += a[-1]
            return ans
        else:
            for x, y in zip(b, a):
                ans += x + y
            ans += b[-1]
            return ans
