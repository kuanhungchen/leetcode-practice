class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k != 0:
            times = len(nums) - k % len(nums)
            for _ in range(times):
                tmp = nums.pop(0)
                nums.append(tmp)


class Solution2:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or k == 0:
            return
        for i in range(k):
            if i < k:
                nums[i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[i]
        nums[k:] = sorted(nums[k:])


class Solution3:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
