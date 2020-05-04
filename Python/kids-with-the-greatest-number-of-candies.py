class Solution:
    def kidsWithCandies(self, cs, ex):
        mx = max(cs)
        ans = []
        for c in cs:
            if c + ex >= mx:
                ans.append(True)
            else:
                ans.append(False)
        return ans
