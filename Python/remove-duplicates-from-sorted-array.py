class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 2:
            return len(nums)
        idx = 1
        while idx != len(nums):
            if nums[idx] == nums[idx-1]:
                nums.pop(idx)
                idx -= 1
            idx += 1
        return len(nums)


class Solution2:
    def removeDuplicates(self, nums):
        # kind of two-pointer
        # refer to others
        if len(nums) < 2:
            return len(nums)
        k = 1
        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[k] = nums[i]
                k += 1
        return k
