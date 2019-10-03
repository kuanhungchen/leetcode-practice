class Solution:
    def smallestRangeII(self, A, K):
        A.sort()
        ans = A[-1] - A[0]
        for i in range(len(A)-1):
            _max = max(A[-1], A[i]+2*K)
            _min = min(A[i+1], A[0]+2*K)
            ans = min(ans, _max-_min)
        return ans
