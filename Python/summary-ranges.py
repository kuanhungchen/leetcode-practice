class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        _last = _start = nums[0]
        ans = []
        for idx in range(1, len(nums)):
            if nums[idx] != _last + 1:
                if _start != _last:
                    ans.append(str(_start)+"->"+str(_last))
                else:
                    ans.append(str(_last))
                _start = nums[idx]
            _last = nums[idx]
        if _start != _last:
            ans.append(str(_start) + "->" + str(_last))
        else:
            ans.append(str(_last))
        return ans
