class Solution:
    def longestArithSeqLength(self, nums):
        dp = {}
        for i, numi in enumerate(nums):
            for j, numj in enumerate(nums[:i]):
                diff = numj - numi
                dp[(i, diff)] = 2 if (j, diff) not in dp else dp[(j, diff)] + 1
        return max(dp.values())
