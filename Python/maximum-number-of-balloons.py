class Solution:
    def maxNumberOfBalloons(self, t):
        from collections import Counter
        c = Counter(t)
        return min(c['b'], c['a'], c['l'] // 2, c['o'] // 2, c['n'])
