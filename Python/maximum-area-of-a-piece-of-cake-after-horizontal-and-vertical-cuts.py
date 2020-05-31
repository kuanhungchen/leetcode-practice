class Solution:
    def maxArea(self, h, w, hs, vs):
        MOD = 10 ** 9 + 7
        hs.append(h)
        vs.append(w)
        hs.sort()
        vs.sort()

        hmx = last = hs[0]
        for h in hs[1:]:
            if h - last > hmx:
                hmx = h - last
            last = h

        vmx = last = vs[0]
        for v in vs[1:]:
            if v - last > vmx:
                vmx = v - last
            last = v

        return (hmx * vmx) % MOD
