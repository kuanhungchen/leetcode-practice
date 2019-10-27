class Solution:
    def maximumSum(self, arr):
        if len(arr) == 1:
            return arr[0]
        dp = [[-1, -1] for _ in range(len(arr))]
        dp[0] = [arr[0], arr[0]]
        res = -10 ** 6
        for i in range(1, len(arr)):
            dp[i][0] = max(dp[i-1][0] + arr[i], dp[i-1][1])
            dp[i][1] = max(dp[i-1][1] + arr[i], arr[i])
            res = max(res, dp[i][0], dp[i][1])
        return res
