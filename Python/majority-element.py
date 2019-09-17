class Solution:
    def majorityElement(self, nums):
        return sorted(nums)[len(nums)//2]


class Solution2:
    # more quick
    def majorityElement(self, nums):
        s = set(nums)
        for item in s:
            if nums.count(item) > len(nums) // 2:
                return item