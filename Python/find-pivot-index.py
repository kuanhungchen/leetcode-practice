class Solution:
    def pivotIndex(self, nums):
        if len(nums) == 0:
            return -1

        total = sum(nums)
        sums = [0]
        for idx in range(len(nums)):
            if 2 * sums[-1] + nums[idx] == total:
                return idx
            else:
                sums.append(sums[-1]+nums[idx])
        return -1
