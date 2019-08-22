class Solution:
    def dominantIndex(self, nums):
        # if not nums:
        #     return -1
        first_max = -1
        second_max = -1
        max_idx = -1
        for idx in range(len(nums)):
            if nums[idx] > first_max:
                second_max = first_max
                first_max = nums[idx]
                max_idx = idx
            elif nums[idx] > second_max:
                second_max = nums[idx]
        if first_max >= 2 * second_max:
            return max_idx
        else:
            return -1

        # for idx in range(len(nums)):
        #     if nums[idx] > first_max:
        #         second_max = first_max
        #         first_max = nums[idx]
        #         max_idx = idx
        #
        # nums.pop(max_idx)
        # nums = [2*x for x in nums]
        # for num in nums:
        #     if num > _max:
        #         return -1
        # return max_idx


example = []
sln = Solution()
print(sln.dominantIndex(example))
