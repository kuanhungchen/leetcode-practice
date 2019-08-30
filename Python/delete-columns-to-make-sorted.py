class Solution:
    def minDeletionSize(self, A):
        ans = 0
        for idx in range(len(A[0])):
            for string_idx in range(len(A)-1):
                if ord(A[string_idx+1][idx]) < ord(A[string_idx][idx]):
                    ans += 1
                    break
        return ans


class Solution2:
    def minDeletionSize(self, A):
        ans = 0
        _range = list(range(len(A[0])))
        for string_idx in range(len(A)-1):
            for idx in _range:
                if ord(A[string_idx+1][idx]) < ord(A[string_idx][idx]):
                    ans += 1
                    _range.remove(idx)

        return ans


class Solution3:
    def minDeletionSize(self, A):
        # cool solution, copy from others
        ans = 0
        for l in zip(*A):
            if list(l) != sorted(l):
                ans += 1
        return ans
