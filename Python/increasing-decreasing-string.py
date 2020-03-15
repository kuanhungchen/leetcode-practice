class Solution:
    def sortString(self, s):
        maps = {}
        for c in s:
            if c in maps:
                maps[c] += 1
            else:
                maps[c] = 1
        keys = maps.keys()
        keys = sorted(keys)

        ans = ""
        while True:
            for k in keys:
                if maps[k]:
                    maps[k] -= 1
                    ans += k
            if len(ans) == len(s): return ans
            tmp = ""
            for k in keys:
                if maps[k]:
                    maps[k] -= 1
                    tmp += k
            ans += tmp[::-1]
            if len(ans) == len(s): return ans
