class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        # ans = [nums[2*i] for i in range(int(len(nums)/2))]
        ans = nums[::2]
        return sum(ans)
