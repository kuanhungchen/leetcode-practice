class Solution:
    def maxUncrossedLines(self, A, B):
        m, n = len(A), len(B)
        dp = [0 for _ in range(n + 1)]
        for i in range(m):
            for j in range(n):
                if A[i] == B[n - 1 - j]:
                    dp[n - j] = dp[n - 1 - j] + 1
            for j in range(n):
                dp[j + 1] = max(dp[j + 1], dp[j])

        return dp[n]
