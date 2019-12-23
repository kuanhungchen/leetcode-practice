class Solution:
    def maxFreq(self, s, maxL, minS, maxS):
        mx = len(s) - maxS + 1
        ans = 0
        for size in range(minS, maxS + 1):
            d = {}
            a = {}
            for i in range(len(s) - size + 1):
                subS = s[i:i + size]
                if not len(d):
                    for c in subS:
                        if c not in d: d[c] = 1
                        else: d[c] += 1
                else:
                    if d[toD] == 1: del d[toD]
                    else: d[toD] -= 1
                    if subS[-1] not in d: d[subS[-1]] = 1
                    else: d[subS[-1]] += 1
                if len(d) <= maxL:
                    if subS not in a: a[subS] = 1
                    else: a[subS] += 1
                toD = subS[0]
            if len(a.values()): ans = max(ans, max(a.values()))
            if ans >= mx: return ans
        return ans
