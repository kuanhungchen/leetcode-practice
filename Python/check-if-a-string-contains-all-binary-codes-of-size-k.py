class Solution:
    def hasAllCodes(self, s, k):

        def solve(s, l):
            return s in mp if l == k else solve(s + '0', l + 1) and solve(s + '1', l + 1)

        window = 0
        mp = set()
        cur = ""
        for i, c in enumerate(s):
            if window != k:
                cur += c
                window += 1
            else:
                cur = cur[1:] + c
            if window == k:
                mp.add(cur)

        return solve("", 0)
