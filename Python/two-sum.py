class Solution:
    def twoSum(self, nums, target):
        # Time: O(nlgn), if nums is sorted, time can be O(n)
        # Space: O(n), if nums is sorted, space can be O(1)
        tmp = nums
        nums = sorted(tmp)
        small = 0
        large = len(nums) - 1
        current = nums[0] + nums[large]
        while current != target:
            if current < target:
                small += 1
            elif current > target:
                large -= 1
            current = nums[small] + nums[large]

        if nums[small] == nums[large]:
            first_idx = tmp.index(nums[small])
            return [first_idx, tmp[first_idx+1:].index(nums[large])+first_idx+1]
        return [min(tmp.index(nums[small]), tmp.index(nums[large])),
                max(tmp.index(nums[small]), tmp.index(nums[large]))]


class Solution2:
    def twoSum(self, nums, target):
        # Time: O(n)
        # Space: O(n)
        _dict = {}
        for idx in range(len(nums)):
            if target - nums[idx] in _dict:
                return [_dict[target - nums[idx]], idx]
            _dict[nums[idx]] = idx
