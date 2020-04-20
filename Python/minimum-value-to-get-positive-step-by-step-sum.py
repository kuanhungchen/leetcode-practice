class Solution:
    def minStartValue(self, nums):
        mn = 1000
        cnt = 0
        for num in nums:
            cnt += num
            mn = min(mn, cnt)
        return 1 - mn if 1 - mn > 0 else 1
