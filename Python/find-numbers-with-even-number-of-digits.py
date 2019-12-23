class Solution:
    def findNumbers(self, nums):
        ans = 0
        for num in nums:
            cnt = 0
            while num:
                cnt += 1
                num //= 10
            ans += 1 if not cnt % 2 else 0
        return ans
