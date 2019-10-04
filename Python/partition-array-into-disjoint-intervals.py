class Solution:
    def partitionDisjoint(self, A):
        max_now = candidate = A[0]
        _len = 1
        for i in range(1, len(A)):
            if A[i] < max_now:
                _len = i + 1
                max_now = candidate
            else:
                if A[i] > candidate:
                    candidate = A[i]
        return _len
