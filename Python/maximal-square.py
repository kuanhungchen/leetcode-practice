class Solution:
    def maximalSquare(self, mat):
        if not mat: return 0
        dp = [[0 for _ in range(len(mat[0]) + 1)] for _ in range(len(mat) + 1)]
        maxlen = 0
        for i, row in enumerate(mat):
            for j, ele in enumerate(row):
                if ele == '1':
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    maxlen = max(maxlen, dp[i+1][j+1])
        return maxlen * maxlen
