class Solution:
    def canConstruct(self, s, k):
        odds = {}
        for c in s:
            if c in odds:
                odds[c] = not odds[c]
            else:
                odds[c] = True
        od = sum([1 for x in odds.values() if x])
        return od <= k <= len(s)
