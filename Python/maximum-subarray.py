class Solution:
    def maxSubArray(self, nums):
        # dp[i] means the max sum contains nums[i]
        # When loop goes to index i, we decide dp[i] to be
        # either dp[i-1]+num[i] or num[i].
        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for idx in range(1, len(nums)):
            dp[idx] = max(dp[idx-1]+nums[idx], nums[idx])
        return max(dp)
