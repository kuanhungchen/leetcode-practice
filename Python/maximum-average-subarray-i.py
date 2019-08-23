class Solution:
    def findMaxAverage(self, nums, k):
        _max = _now = sum(nums[:k])
        for idx in range(1, len(nums)-k+1):
            _now = _now - nums[idx-1] + nums[idx+k-1]
            _max = max(_now, _max)
        return _max / float(k)


example = [1, 12, -5, -6, 50, 3, 77, 30, 100, -6, -15, 1, 37]
_k = 4
sln = Solution()
print(sln.findMaxAverage(example, _k))
