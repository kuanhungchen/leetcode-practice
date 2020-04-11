class Solution:
    def numSteps(self, s):
        ans = 0
        while s != "1":
            ans += 1
            if s[-1] == "1":
                s = bin(int(s, 2) + 1)[2:]
            else:
                s = s[:-1]
        return ans
