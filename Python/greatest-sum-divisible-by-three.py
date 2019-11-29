class Solution:
    def maxSumDivThree(self, nums):
        dp = [[0, 0, 0] for _ in range(len(nums))]
        dp[0][nums[0] % 3] = nums[0]
        for i in range(1, len(nums)):
            for j in range(3):
                s = dp[i-1][(j - nums[i]) % 3] + nums[i]
                if s % 3 == j:
                    dp[i][j] = max(dp[i-1][j], s)
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][0]
