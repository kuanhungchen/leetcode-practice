class Solution:
    def largestSumAfterKNegations(self, A, K):
        for _ in range(K):
            target = min(A)
            A.remove(target)
            A.append(-target)
        return sum(A)
