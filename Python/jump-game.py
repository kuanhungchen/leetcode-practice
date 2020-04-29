class Solution:
    def canJump(self, nums):
        dp = [False for _ in range(len(nums))]
        dp[-1] = True
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                dp[i] = 1 if type(dp[i + 1]) is bool else dp[i + 1] + 1
            else:
                if type(dp[i + 1]) is not bool:
                    if nums[i] > dp[i + 1]:
                        dp[i] = dp[i + 1 + dp[i + 1]]
                    else:
                        dp[i] = dp[i + 1] + 1
                else:
                    dp[i] = dp[i + 1]
        if type(dp[0]) is not bool: return False
        return dp[0]


class Solution2:
    def canJump(self, nums):
        last_position = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if (i + nums[i]) >= last_position:
                last_position = i
        return last_position == 0
