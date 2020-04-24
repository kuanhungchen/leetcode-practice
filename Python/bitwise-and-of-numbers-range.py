class Solution:
    def rangeBitwiseAnd(self, m, n):
        mb = bin(m)[2:]
        nb = bin(n)[2:]
        r = max(len(nb) - len(mb), 0)
        mb = '0' * r + mb
        ans = 0
        for i in range(r, len(nb)):
            if mb[i] == '1' and nb[i] == '1' and (n - m) <= 2 ** (len(nb) - i - 1):
                ans += 2 ** (len(mb) - i - 1)
        return ans
