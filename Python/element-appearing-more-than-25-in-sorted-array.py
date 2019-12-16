class Solution:
    def findSpecialInteger(self, arr):
        from collections import Counter
        ctr = Counter(arr)
        return ctr.most_common(1)[0][0]
