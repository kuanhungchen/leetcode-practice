class Solution:
    def numJewelsInStones(self, J, S):
        js = set(J)
        ans = 0
        for s in S:
            if s in js:
                ans += 1
        return ans
