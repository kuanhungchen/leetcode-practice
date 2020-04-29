class Solution:
    def longestCommonSubsequence(self, s1, s2):
        dp = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                if c1 == c2:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]
