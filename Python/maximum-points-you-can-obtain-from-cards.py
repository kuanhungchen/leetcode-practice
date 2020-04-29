class Solution:
    def maxScore(self, cards, k):
        pre = [0]
        for card in cards:
            pre.append(pre[-1] + card)
        ans = 0
        n = len(pre)
        for i in range(k + 1):
            ans = max(pre[i] + pre[-1] - pre[n - 1 - k + i], ans)
        return ans
