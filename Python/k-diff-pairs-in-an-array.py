class Solution:
    def findPairs(self, nums, k):
        if k == 0:
            _dict = {}
            ans = 0
            for num in nums:
                if num in _dict.keys():
                    if _dict[num] == 1:
                        ans += 1
                        _dict[num] = -1
                else:
                    _dict[num] = 1
            return ans

        nums = sorted(list(set(nums)))
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] - nums[i] == k:
                    ans += 1
                if nums[j] - nums[i] > k:
                    break
        return ans
