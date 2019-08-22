class Solution:
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
        for idx in range(len(nums)):
            if nums[idx] >= target:
                return idx
        return len(nums)


example = [1, 2]
t = 2
sln = Solution()
print(sln.searchInsert(example, t))
