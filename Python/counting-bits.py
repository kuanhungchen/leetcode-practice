class Solution:
    def countBits(self, num):
        ans = [0]
        while len(ans) <= num:
            ans += [i + 1 for i in ans]
        return ans[:num + 1]
