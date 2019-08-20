class Solution:
    def findLengthOfLCIS(self, nums):
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        _max = 1
        c = 1
        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx-1]:
                c += 1
            else:
                c = 1
            if c > _max:
                _max = c
        return _max
