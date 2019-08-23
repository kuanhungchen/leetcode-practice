class Solution:
    def containsNearbyDuplicate(self, nums, k):
        _dict = {}
        for idx in range(len(nums)):
            if nums[idx] in _dict.keys():
                if idx - _dict[nums[idx]] <= k:
                    return True
            _dict[nums[idx]] = idx
        return False
