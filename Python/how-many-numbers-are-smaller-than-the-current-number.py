class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans = [0 for _ in range(len(nums))]
        for i, num in enumerate(nums):
            for _num in nums:
                ans[i] += _num < num
        return ans
