class Solution:
    def smallestRangeI(self, A, K):
        if len(A) == 1:
            return 0
        _max = max(A)
        _min = min(A)
        diff = _max - _min
        if diff > 2 * K:
            return diff - 2 * K
        else:
            return 0
