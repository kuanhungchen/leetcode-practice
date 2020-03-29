class Solution:
    def decompressRLElist(self, nums):
        ans = []
        i = 0
        while i != len(nums):
            fre = nums[i]
            ele = nums[i + 1]
            i += 2
            ans.extend([ele for _ in range(fre)])
        return ans
