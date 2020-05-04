class Solution:
    def kLengthApart(self, nums, k):
        n = len(nums)
        i = 0
        while i + k + 1 < n:
            sm = sum(nums[i:i + k + 1])
            if sm > 1: return False
            i += k + 1
        return sum(nums[i:]) <= 1
