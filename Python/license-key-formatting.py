class Solution:
    def licenseKeyFormatting(self, S, K):
        ans = ""
        cnt = 0
        for c in S[::-1]:
            if c == '-': continue
            ans += c.upper()
            cnt += 1
            if ans and cnt % K == 0: ans += '-'
        return ans[-2::-1] if ans and ans[-1] == '-' else ans[::-1]
