class Solution:
    def maxScore(self, s):
        zpre = [0]
        opre = [0]
        for c in s:
            if c == '0':
                zpre.append(zpre[-1] + 1)
                opre.append(opre[-1])
            else:
                opre.append(opre[-1] + 1)
                zpre.append(zpre[-1])
        ans = 0
        for i in range(1, len(s)):
            ans = max(ans, zpre[i] + opre[-1] - opre[i])
        return ans
