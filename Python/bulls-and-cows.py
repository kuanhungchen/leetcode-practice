class Solution:
    def getHint(self, secret, guess):
        ss, gs = {str(x): 0 for x in range(10)}, {str(x): 0 for x in range(10)}
        A = 0
        for s, g in zip(secret, guess):
            if s == g: A += 1
            ss[s] += 1
            gs[g] += 1

        ans = 0
        for k, v in ss.items():
            ans += min(v, gs[k])

        return str(A) + "A" + str(ans - A) + "B"
