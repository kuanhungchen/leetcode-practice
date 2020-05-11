class Solution:
    def findContentChildren(self, g, s):
        ans = 0

        s.sort()
        g.sort()

        i, j = 0, 0
        while i < len(s) and j < len(g):
            while i < len(s) and j < len(g) and s[i] < g[j]:
                i += 1

            if i >= len(s):
                break

            i += 1
            j += 1
            ans += 1

        return ans
