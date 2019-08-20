class Solution:
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for idx in range(2, len(nums)):
            dp[idx] = max(nums[idx]+dp[idx-2], dp[idx-1])

        return dp[-1]
