class Solution:
    def minSubsequence(self, nums):
        nums = sorted(nums, reverse=True)
        sm = sum(nums)
        res = 0
        ans = []
        for num in nums:
            if res > sm - res:
                return ans
            res += num
            ans.append(num)
        return ans
