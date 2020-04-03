class Solution:
    def longestPrefix(self, s):
        pre, suf, ans, mod, tmp = 0, 0, 0, 10 ** 9 + 7, 1
        for i in range(len(s) - 1):
            pre = (pre * 64 + ord(s[i])) % mod
            suf = (ord(s[~i]) * tmp + suf) % mod
            tmp = (tmp * 64) % mod
            if pre == suf: ans = i + 1
        return s[:ans]
