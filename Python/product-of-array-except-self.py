class Solution:
    def productExceptSelf(self, nums):
        ans = [1] * len(nums)
        p = 1
        for i in range(len(ans)):
            ans[i] *= p
            p *= nums[i]
        p = 1
        for i in range(len(ans)-1, -1, -1):
            ans[i] *= p
            p *= nums[i]
        return ans
