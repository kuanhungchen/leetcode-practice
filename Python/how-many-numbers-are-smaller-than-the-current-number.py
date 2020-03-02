class Solution:
    def smallerNumbersThanCurrent(self, nums):
        ans = []
        for num in nums:
            ans.append(sum([x < num for x in nums]))
        return ans
