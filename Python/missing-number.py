class Solution:
    def missingNumber(self, nums):
        # smary solution from leetcode
        return (1+len(nums)) * len(nums) // 2 - sum(nums)
